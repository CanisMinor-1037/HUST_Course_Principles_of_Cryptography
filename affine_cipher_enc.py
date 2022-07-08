#!/usr/bin/python3
# @File : affine_cipher_enc.py
# @Author : CanisMinor
# @Date : 2022-07-08
a = 7
b = 3
plaintext = input("请输入明文: ")
plaintext = plaintext.lower()
ciphertext = ""

for letter in plaintext:
    number = ord(letter)
    if number in range(0x61, 0x61 + 26):
        number -= 0x61
        number = (number * a + b) % 26
        ciphertext += chr(number + 0x61)
    else:
        ciphertext += letter

ciphertext = ciphertext.upper()
print(f"密文为: {ciphertext}")