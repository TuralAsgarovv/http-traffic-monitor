import sys
import yaml
import os
from sniffer import HTTPSniffer
from utils import setup_logging

def load_config(config_path: str) -> dict:
    """
    YAML konfiqurasiya faylını yükləyir.
    """
    if not os.path.exists(config_path):
        print(f"Xəta: Konfiqurasiya faylı tapılmadı - {config_path}")
        sys.exit(1)
        
    with open(config_path, 'r') as file:
        try:
            return yaml.safe_load(file)
        except yaml.YAMLError as exc:
            print(f"YAML parsing xətası: {exc}")
            sys.exit(1)

def main():
    # Konfiqurasiyanın yüklənməsi
    config_path = os.path.join("config", "settings.yaml")
    config = load_config(config_path)

    # Loglama sisteminin qurulması
    setup_logging(config.get('log_file', 'traffic.log'))
    
    interface = config.get('interface', 'eth0')
    bpf_filter = config.get('filter_expression', 'tcp port 80')

    # Sniffer obyektinin yaradılması
    sniffer = HTTPSniffer(interface=interface, bpf_filter=bpf_filter)

    try:
        sniffer.start()
    except KeyboardInterrupt:
        print("\n[!] Proqram istifadəçi tərəfindən dayandırıldı.")
        sys.exit(0)

if __name__ == "__main__":
    main()