#!/usr/bin/python3
# @File : permutation_cipher_dec.py
# @Author : CanisMinor
# @Date : 2022-07-08
pi = {
    1: 3,
    2: 5,
    3: 1,
    4: 6,
    5: 4,
    6: 2,
}
inv_pi = {}
for key, value in pi.items():
    inv_pi[value] = key
ciphertext = input("请输入密文: ")
ciphertext = ciphertext.lower()
#填充
length = len(ciphertext)
ciphertext += (6 - length % 6) * ' '
#print(len(ciphertext)%6==0)
blocks_num = len(ciphertext) / 6
plaintext = ""
for base in range(int(blocks_num)):
    for offset in range(6):
        plaintext += ciphertext[base * 6 + inv_pi[offset + 1] - 1]
plaintext = plaintext.lower().replace(' ', '')
print(f"明文为: {plaintext}")