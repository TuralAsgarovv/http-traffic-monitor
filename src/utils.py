import logging
import sys
from typing import Optional

def setup_logging(log_path: str) -> None:
    """
    Loglama sistemini sazlayır.
    Loglar həm fayla, həm də konsola yazılacaq.
    """
    # Log formatını təyin edirik
    log_format = '%(asctime)s - %(levelname)s - %(message)s'
    
    logging.basicConfig(
        level=logging.INFO,
        format=log_format,
        handlers=[
            logging.FileHandler(log_path),
            logging.StreamHandler(sys.stdout)
        ]
    )
    
    # TODO: Log səviyyəsini konfiqurasiyadan oxumaq üçün tənzimləmə əlavə et.
    logging.info(f"Loglama sistemi aktivdir. Fayl: {log_path}")

def validate_interface(interface_name: str) -> bool:
    """
    İnterfeys adının doğruluğunu yoxlayır (sadə yoxlama).
    """
    if not interface_name or len(interface_name) == 0:
        return False
    return True
