#!/bin/bash

# Rəngli çıxış üçün
GREEN='\033[0;32m'
NC='\033[0m' # No Color

echo -e "${GREEN}[+] Quraşdırma başlayır...${NC}"

# Virtual mühitin yaradılması
if [ ! -d "venv" ]; then
    echo -e "${GREEN}[+] Python virtual mühiti yaradılır...${NC}"
    python3 -m venv venv
fi

# Aktivləşdir və asılılıqları yüklə
source venv/bin/activate

echo -e "${GREEN}[+] Asılılıqlar yüklənir (pip)...${NC}"
pip install -r requirements.txt

echo -e "${GREEN}[+] Qovluqlar yoxlanılır...${NC}"
mkdir -p logs

echo -e "${GREEN}[+] Hazırdır! Proqramı işə salmaq üçün:${NC}"
echo "source venv/bin/activate"
echo "sudo python3 src/main.py"