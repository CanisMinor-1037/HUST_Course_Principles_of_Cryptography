#!/usr/bin/python3
# @File : caesar_cipher_enc.py
# @Author : CanisMinor
# @Date : 2022-07-08
key = 3
plaintext = input("请输入明文: ")
plaintext = plaintext.lower()
ciphertext = ""

for letter in plaintext:
    number = ord(letter)
    if number in range(0x61, 0x61 + 26):
        number = (number - 0x61 + key) % 26
        ciphertext += chr(0x61 + number)
    else:
        ciphertext += letter

ciphertext = ciphertext.upper()
print(f"密文为: {ciphertext}")