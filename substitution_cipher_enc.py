# substitution_cipher_enc.py
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
plaintext = input("请输入明文: ")
plaintext = plaintext.lower()
ciphertext = ""

for letter in plaintext:
    number = ord(letter)
    if number in range(0x61, 0x61 + 26):
        ciphertext += s_box[letter]
    else:
        ciphertext += letter

ciphertext = ciphertext.upper()
print(f"密文为: {ciphertext}")