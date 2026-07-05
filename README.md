# 🔐 Parola Üreticisi

> Kriptografik olarak güvenli, sıfır bağımlılıklı bir komut satırı parola üreticisi.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.6%2B-3776AB.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![No Dependencies](https://img.shields.io/badge/dependencies-none-brightgreen.svg?style=for-the-badge)](#-kullanılan-teknolojiler)

Python'un `secrets` modülünü kullanarak kriptografik olarak güvenli parolalar üreten küçük bir komut satırı aracıdır. Harici bir bağımlılığı yoktur; yalnızca Python standart kütüphanesiyle çalışır.

## 🎬 Demo

```console
$ python3 passgen.py
#S!w!IHxhAVW3Ydf

Güç: çok güçlü 💪

$ python3 passgen.py -l 20 -n 3 --no-symbols
A3AmciWMgWQQzu9o2uNy
liAibrT05O8gtjv68owU
vcznKoJ8JSYQ4eDtYjhZ

Güç: güçlü ✅
```

## ✨ Özellikler

- 🔒 Kriptografik olarak güvenli rastgelelik (`secrets` modülü)
- 📏 Ayarlanabilir parola uzunluğu
- 🔢 Rakam ve sembolleri açıp kapatabilme
- 🔁 Tek seferde birden fazla parola üretme
- 💪 Basit güç göstergesi
- ✅ Her parolada büyük/küçük harf çeşitliliği garantisi
- 📦 Sıfır üçüncü parti bağımlılık — yalnızca standart kütüphane

## 🚀 Kurulum & Çalıştırma

Kurulum gerektirmez. Python 3.6 veya üzeri yeterlidir.

```bash
git clone https://github.com/tasocuk/password-generator.git
cd password-generator
python3 passgen.py
```

## 📖 Kullanım

```bash
python3 passgen.py                 # 16 karakterlik varsayılan parola
python3 passgen.py -l 24           # 24 karakterlik parola
python3 passgen.py -n 5            # 5 adet parola üret
python3 passgen.py --no-symbols    # sembol kullanma
python3 passgen.py --no-digits     # rakam kullanma
python3 passgen.py -h              # yardım
```

| Seçenek | Açıklama | Varsayılan |
| --- | --- | --- |
| `-l`, `--length` | Parola uzunluğu (en az 4) | `16` |
| `-n`, `--count` | Üretilecek parola sayısı | `1` |
| `--no-symbols` | Sembolleri kullanma | (kapalı) |
| `--no-digits` | Rakamları kullanma | (kapalı) |

### Testler

Testler yalnızca standart kütüphaneyle (`unittest`) yazılmıştır:

```bash
python3 -m unittest -v
```

## 🛠️ Kullanılan Teknolojiler

- **Python 3** (3.6+)
- Standart kütüphane: `argparse`, `secrets`, `string`
- Testler: `unittest`
- Üçüncü parti bağımlılık yok

## 📁 Proje Yapısı

```text
password-generator/
├── passgen.py          # Ana komut satırı aracı
├── test_passgen.py     # unittest birim testleri
├── README.md
├── LICENSE
└── .gitignore
```

## 📄 Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Ayrıntılar için [LICENSE](LICENSE) dosyasına bakın.

## 👤 Geliştirici

**Tahsin Karabulut**
GitHub: [@tasocuk](https://github.com/tasocuk)
