#!/usr/bin/env python3
"""Basit ve güvenli parola üreticisi.

Kullanım örnekleri:
    python passgen.py                 # 16 karakterlik varsayılan parola
    python passgen.py -l 24           # 24 karakterlik parola
    python passgen.py -n 5            # 5 adet parola üret
    python passgen.py --no-symbols    # sembol kullanma
"""

import argparse
import secrets
import string


def generate_password(length: int, use_symbols: bool, use_digits: bool) -> str:
    """Güvenli rastgele parola üretir (random yerine secrets kullanıyorum).

    Her karakter havuzundan bir tane garanti alıyorum, böylece parolada
    en az bir küçük/büyük harf, seçildiyse rakam ve sembol oluyor.
    """
    if length < 4:
        raise ValueError("Parola uzunluğu en az 4 olmalı.")

    pools = [string.ascii_lowercase, string.ascii_uppercase]
    if use_digits:
        pools.append(string.digits)
    if use_symbols:
        pools.append("!@#$%^&*()-_=+[]{}")

    alphabet = "".join(pools)

    # önce her gruptan birer tane al (çeşitlilik garanti), gerisini rastgele doldur
    password = [secrets.choice(pool) for pool in pools]
    password += [secrets.choice(alphabet) for _ in range(length - len(pools))]

    # yoksa hep aynı sırayla başlıyor, karıştıralım
    secrets.SystemRandom().shuffle(password)
    return "".join(password)


def strength_label(length: int, use_symbols: bool, use_digits: bool) -> str:
    """Basit bir güç göstergesi döndürür."""
    score = length
    if use_symbols:
        score += 6
    if use_digits:
        score += 4

    if score >= 26:
        return "çok güçlü 💪"
    if score >= 18:
        return "güçlü ✅"
    if score >= 12:
        return "orta ⚠️"
    return "zayıf ❌"


def main() -> None:
    parser = argparse.ArgumentParser(description="Güvenli parola üreticisi")
    parser.add_argument("-l", "--length", type=int, default=16,
                        help="Parola uzunluğu (varsayılan: 16)")
    parser.add_argument("-n", "--count", type=int, default=1,
                        help="Üretilecek parola sayısı (varsayılan: 1)")
    parser.add_argument("--no-symbols", action="store_true",
                        help="Sembolleri kullanma")
    parser.add_argument("--no-digits", action="store_true",
                        help="Rakamları kullanma")
    args = parser.parse_args()

    use_symbols = not args.no_symbols
    use_digits = not args.no_digits

    for _ in range(args.count):
        pwd = generate_password(args.length, use_symbols, use_digits)
        print(pwd)

    label = strength_label(args.length, use_symbols, use_digits)
    print(f"\nGüç: {label}")


if __name__ == "__main__":
    main()
