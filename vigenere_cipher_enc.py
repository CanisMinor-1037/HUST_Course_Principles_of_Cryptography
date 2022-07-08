#!/usr/bin/python3
# @File : vigenere_cipher_enc.py
# @Author : CanisMinor
# @Date : 2022-07-08

# 密钥字
key = input("请输入密钥字: ")
key = key.lower()

# 密钥字对应的数字串
block_length = len(key)
key_number = []
for i in range(block_length):
    key_number.append(ord(key[i]) - 0x61)
#print(key_number)

# 明文
plaintext = input("请输入明文: ")
plaintext = plaintext.lower()

# 填充
padding_length = block_length - len(plaintext) % block_length
plaintext += padding_length * ' '
block_number = int(len(plaintext) / block_length)

# 加密
ciphertext = ""
for base in range(block_number):
    for offset in range(block_length):
        number = ord(plaintext[base * block_length + offset]) - 0x61
        if number in range(26):
            number = (number + key_number[offset]) % 26
        ciphertext += chr(0x61 + number)

ciphertext = ciphertext[:-padding_length].upper()
print(f"密文为: {ciphertext}")