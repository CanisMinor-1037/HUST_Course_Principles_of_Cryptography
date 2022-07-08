#!/usr/bin/python3
# @File : substitution_cipher_dec.py
# @Author : CanisMinor
# @Date : 2022-07-08
s_box = {
    'a': 'x',
    'b': 'n',
    'c': 'y',
    'd': 'a',
    'e': 'h',
    'f': 'p',
    'g': 'o',
    'h': 'g',
    'i': 'z',
    'j': 'q',
    'k': 'w',
    'l': 'b',
    'm': 't',
    'n': 's',
    'o': 'f',
    'p': 'l',
    'q': 'r',
    'r': 'c',
    's': 'v',
    't': 'm',
    'u': 'u',
    'v': 'e',
    'w': 'k',
    'x': 'j',
    'y': 'd',
    'z': 'i'
}

inv_s_box = {}

for key, value in s_box.items():
    inv_s_box[value] = key

ciphertext = input("请输入密文: ")
ciphertext = ciphertext.lower()
plaintext = ""

for letter in ciphertext:
    number = ord(letter)
    if number in range(0x61, 0x61 + 26):
        plaintext += inv_s_box[letter]
    else:
        plaintext += letter

print(f"明文为: {plaintext}")