# HTTP Trafik Monitoru

![Status](https://img.shields.io/badge/status-active-green) ![Language](https://img.shields.io/badge/python-3.9+-blue) ![License](https://img.shields.io/badge/license-MIT-orange)

## Giriş

**HTTP Trafik Monitoru**, şəbəkə interfeysini dinləyən və HTTP paketlərini (xüsusilə başlıqları/headers) analiz edən Python əsaslı bir vasitədir. Bu layihə kiber təhlükəsizlik mütəxəssisləri və tələbələr üçün şəbəkə protokollarını daha dərindən başa düşmək məqsədilə hazırlanmışdır.

> **XƏBƏRDARLIQ:** Bu proqram yalnız təhsil və qorunma məqsədləri üçün nəzərdə tutulmuşdur. İcazəniz olmayan şəbəkələrdə istifadə etməyin.

## Xüsusiyyətlər

- Real vaxt rejimində paketlərin tutulması (Sniffing).
- HTTP sorğularının avtomatik filtrlənməsi.
- İstifadəçi tərəfindən tənzimlənən konfiqurasiya faylı.
- Ətraflı loglama sistemi.

## Quraşdırma

Layihəni klonlayın və asılılıqları quraşdırın:

```bash
git clone https://github.com/username/http-traffic-monitor.git
cd http-traffic-monitor
./setup.sh
```

Alternativ olaraq Docker istifadə edə bilərsiniz:

```bash
docker build -t http-monitor .
```

## İstifadə

Proqramı işə salmaq üçün (root hüquqları tələb oluna bilər):

```bash
sudo python3 src/main.py
```

## Konfiqurasiya

`config/settings.yaml` faylını redaktə edərək interfeys və log faylının yerini dəyişə bilərsiniz.

## Töhfə (Contributing)

Zəhmət olmasa `CONTRIBUTING.md` faylına nəzər yetirin.

## Lisenziya

Bu layihə MIT lisenziyası altında yayımlanır.
