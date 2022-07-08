# permutation_cipher_enc.py
pi = {
    1: 3,
    2: 5,
    3: 1,
    4: 6,
    5: 4,
    6: 2,
    }

plaintext = input("请输入明文: ")
plaintext = plaintext.lower()

#填充
length = len(plaintext)
plaintext += (6 - length%6)*' '
#print(len(plaintext)%6==0)
blocks_num = len(plaintext)/6
ciphertext = ""

for base in range(int(blocks_num)):
    for offset in range(6):
        ciphertext += plaintext[base*6+pi[offset+1]-1]
ciphertext = ciphertext.upper().replace(' ','')
print(f"密文为: {ciphertext}")