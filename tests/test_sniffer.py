import unittest
from unittest.mock import MagicMock, patch
from src.sniffer import HTTPSniffer
from scapy.all import IP, TCP, Raw

class TestHTTPSniffer(unittest.TestCase):
    """
    HTTPSniffer sinifi üçün vahid (unit) testlər.
    """

    def setUp(self):
        """
        Hər testdən əvvəl işə düşür.
        """
        self.sniffer = HTTPSniffer(interface="test_iface", bpf_filter="tcp port 80")
        # Loglamanı 'mock' edirik ki, test zamanı fayl yazılmasın
        self.sniffer.logger = MagicMock()

    def test_process_packet_http(self):
        """
        HTTP məzmunlu paketin düzgün tanınmasını yoxlayır.
        """
        # Saxta bir HTTP paketi yaradırıq
        mock_payload = "GET /index.html HTTP/1.1\r\nHost: example.com\r\n\r\n"
        packet = IP(src="192.168.1.5", dst="1.1.1.1") / TCP(dport=80) / Raw(load=mock_payload.encode())

        self.sniffer.process_packet(packet)

        # Logger-in info metodunun çağırılıb-çağırılmadığını yoxlayırıq
        self.sniffer.logger.info.assert_called()
        # Log mesajında IP-nin olub-olmadığını yoxlayırıq
        args, _ = self.sniffer.logger.info.call_args
        self.assertIn("192.168.1.5", args[0])
        self.assertIn("GET /index.html HTTP/1.1", args[0])

    def test_process_packet_non_http(self):
        """
        HTTP olmayan paketin inkar edilməsini yoxlayır.
        """
        mock_payload = "SSH-2.0-OpenSSH_8.2p1"
        packet = IP(src="192.168.1.5", dst="1.1.1.1") / TCP(dport=22) / Raw(load=mock_payload.encode())

        self.sniffer.process_packet(packet)

        # HTTP olmadığı üçün logger çağırılmamalıdır (info səviyyəsində)
        self.sniffer.logger.info.assert_not_called()

if __name__ == '__main__':
    unittest.main()