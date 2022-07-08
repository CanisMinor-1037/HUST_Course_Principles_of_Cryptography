#!/usr/bin/python3
# @File : polybius_enc.py
# @Author : CanisMinor
# @Date : 2022-07-08
base = 0x61
offset = 0x5
chessboard = {}

for i in range(base, base + offset):
    chessboard[chr(i)] = '1' + chr(i - 0x30)
base += offset

for i in range(base, base + 0x3):
    chessboard[chr(i)] = '2' + chr(i - 0x30 - offset)

chessboard['i'] = '24'
chessboard['j'] = '24'
chessboard['k'] = '25'
base += (offset + 0x1)

for j in range(3, 6):
    for i in range(base, base + offset):
        chessboard[chr(i)] = f'{j}' + chr(i - 0x30 - offset * (j - 1) - 1)
    base += offset
chessboard[' '] = ' '
# print(chessboard)
plaintext = input("请输入明文: ")
plaintext = plaintext.lower()
ciphertext = ""
for letter in plaintext:
    ciphertext += chessboard[letter]
print(f"密文为: {ciphertext}")