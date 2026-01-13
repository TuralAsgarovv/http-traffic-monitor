import logging
from scapy.all import sniff, IP, TCP, Raw
from scapy.packet import Packet
from typing import Callable, Optional

class HTTPSniffer:
    """
    HTTP paketlərini dinləmək və analiz etmək üçün əsas sinif.
    """

    def __init__(self, interface: str, bpf_filter: str):
        """
        Sinifin inisializasiyası.
        
        Args:
            interface (str): Dinləniləcək şəbəkə interfeysi.
            bpf_filter (str): Berkeley Packet Filter ifadəsi.
        """
        self.interface = interface
        self.bpf_filter = bpf_filter
        self.logger = logging.getLogger(__name__)

    def process_packet(self, packet: Packet) -> None:
        """
        Tutulan hər bir paketi emal edən callback funksiyası.
        """
        try:
            # Yalnız Raw məlumatı olan paketlərə baxırıq
            if packet.haslayer(TCP) and packet.haslayer(Raw):
                # Payload-u bayt formatından string-ə çevirməyə çalışırıq
                payload = packet[Raw].load.decode('utf-8', errors='ignore')
                
                # Sadə HTTP yoxlanışı (GET, POST, və s.)
                if "HTTP" in payload:
                    src_ip = packet[IP].src
                    dst_ip = packet[IP].dst
                    
                    # İlk sətri (Request Line) loglayırıq
                    request_line = payload.split('\n')[0].strip()
                    
                    self.logger.info(f"HTTP Paket Tapıldı: {src_ip} -> {dst_ip} | {request_line}")
                    
                    # TODO: Bütün başlıqları (headers) parse edib JSON kimi saxlamaq.
                    
        except Exception as e:
            self.logger.error(f"Paket emalı zamanı xəta baş verdi: {str(e)}")

    def start(self) -> None:
        """
        Dinləmə prosesini başladır.
        """
        self.logger.info(f"Sniffer işə düşür... İnterfeys: {self.interface}, Filtr: {self.bpf_filter}")
        try:
            sniff(
                iface=self.interface,
                filter=self.bpf_filter,
                prn=self.process_packet,
                store=False  # Yaddaş probleminin qarşısını almaq üçün paketləri yadda saxlamırıq
            )
        except PermissionError:
            self.logger.critical("İcazə xətası! Bu skripti 'sudo' ilə işə salmalısınız.")
        except Exception as e:
            self.logger.critical(f"Gözlənilməz xəta: {str(e)}")
