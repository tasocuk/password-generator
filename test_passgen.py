#!/usr/bin/env python3
"""passgen modülü için birim testleri.

Çalıştırma:
    python3 -m unittest -v
"""

import string
import unittest

from passgen import generate_password, strength_label


class GeneratePasswordTest(unittest.TestCase):
    def test_length_is_correct(self):
        for length in (4, 8, 16, 32, 64):
            pwd = generate_password(length, use_symbols=True, use_digits=True)
            self.assertEqual(len(pwd), length)

    def test_no_symbols(self):
        symbols = set("!@#$%^&*()-_=+[]{}")
        for _ in range(50):
            pwd = generate_password(20, use_symbols=False, use_digits=True)
            self.assertFalse(symbols & set(pwd),
                             "Parolada sembol bulunmamalı.")

    def test_no_digits(self):
        for _ in range(50):
            pwd = generate_password(20, use_symbols=True, use_digits=False)
            self.assertFalse(any(ch in string.digits for ch in pwd),
                             "Parolada rakam bulunmamalı.")

    def test_no_symbols_and_no_digits(self):
        pwd = generate_password(20, use_symbols=False, use_digits=False)
        self.assertTrue(all(ch in string.ascii_letters for ch in pwd))

    def test_has_lower_and_upper(self):
        # Çeşitlilik garantisi: her parolada en az bir küçük ve bir büyük harf.
        for _ in range(50):
            pwd = generate_password(8, use_symbols=True, use_digits=True)
            self.assertTrue(any(ch in string.ascii_lowercase for ch in pwd),
                            "En az bir küçük harf olmalı.")
            self.assertTrue(any(ch in string.ascii_uppercase for ch in pwd),
                            "En az bir büyük harf olmalı.")

    def test_length_too_short_raises(self):
        for length in (0, 1, 2, 3, -5):
            with self.assertRaises(ValueError):
                generate_password(length, use_symbols=True, use_digits=True)


class StrengthLabelTest(unittest.TestCase):
    def test_boundaries(self):
        # score = length (+6 sembol, +4 rakam)
        self.assertEqual(strength_label(4, False, False), "zayıf ❌")     # 4
        self.assertEqual(strength_label(11, False, False), "zayıf ❌")    # 11
        self.assertEqual(strength_label(12, False, False), "orta ⚠️")     # 12
        self.assertEqual(strength_label(17, False, False), "orta ⚠️")     # 17
        self.assertEqual(strength_label(18, False, False), "güçlü ✅")     # 18
        self.assertEqual(strength_label(25, False, False), "güçlü ✅")     # 25
        self.assertEqual(strength_label(26, False, False), "çok güçlü 💪")  # 26

    def test_bonuses_applied(self):
        # 16 + 6 + 4 = 26 -> çok güçlü
        self.assertEqual(strength_label(16, True, True), "çok güçlü 💪")
        # 12 + 6 = 18 -> güçlü
        self.assertEqual(strength_label(12, True, False), "güçlü ✅")
        # 8 + 4 = 12 -> orta
        self.assertEqual(strength_label(8, False, True), "orta ⚠️")


if __name__ == "__main__":
    unittest.main()
