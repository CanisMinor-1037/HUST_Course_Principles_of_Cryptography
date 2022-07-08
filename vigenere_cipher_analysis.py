#!/usr/bin/python3
# @File : vigenere_cipher_analysis.py
# @Author : CanisMinor
# @Date : 2022-07-08

#plaintext = "wearediscoveredsaveyourself"
#key = "deceptive"
#ciphertext = "ZICVTWQNGRZGVTWAVZHCQYGLMGJ"
#print(ciphertext)
ciphertext = "CHREEVOAHMAERATBIAXXWTNXBEEOPHBSBQMQEQERBW"
ciphertext += "RVXUOAKXAOSXXWEAHBWGJMMQMNKGRFVGXWTRZXWIAK"
ciphertext += "LXFPSKAUTEMNDCMGTSXMXBTUIADNGMGPSRELXNJELX"
ciphertext += "VRVPRTULHDNQWTWDTYGBPHXTFALJHASVBFXNGLLCHR"
ciphertext += "ZBWELEKMSJIKNBHWRJGNMGJSGLXFEYPHAGNRBIEQJT"
ciphertext += "AMRVLCRREMNDGLXRRIMGNSNRWCHRQHAEYEVTAQEBBI"
ciphertext += "FEEWEVKAKOEWADREMXMTBHHCHRTKDNVRZCHRCLQOHP"
ciphertext += "WQAIIWXNRMGWOIIFKEE"
#print(len(ciphertext))

ciphertext = ciphertext.lower()


def coincidence_index(text):
    """计算文本text的重合指数"""
    letters_frequency = {}
    for i in range(26):
        letter = chr(i + 0x61)
        letters_frequency[letter] = text.count(letter)
    #print(letters_frequency)
    text_length = len(text)
    # Ic = q/p
    p = text_length * (text_length - 1)
    q = 0
    for letter, count in letters_frequency.items():
        q += (count * (count - 1))
    return q / p


def find_str(target_str, text):
    """在文本text中查找target_str序号,返回列表"""
    text_length = len(text)
    start_point = 0
    index_list = []
    while True:
        index = text.find(target_str, start_point, text_length)
        if index != -1:
            index_list.append(index)
            start_point = index + 1
        else:
            break
    return index_list


def shift_text(text, k):
    """对text进行移位变换，密钥为k"""
    result_text = ""
    for letter in text:
        number = ord(letter) - 0x61
        number = (number - k) % 26
        result_text += chr(number + 0x61)
    return result_text


#print(coincidence_index(ciphertext))
#print(find_str('chr',ciphertext))
ciphertext_length = len(ciphertext)
ciphertext_indexs = []
m = 5
for i in range(m):
    ciphertext_index = []
    while i < ciphertext_length:
        ciphertext_index.append(i)
        i += m
    ciphertext_indexs.append(ciphertext_index)
#print(ciphertext_indexs)

i = 0
ciphertext_parts = []
for ciphertext_index in ciphertext_indexs:
    ciphertext_part = ""
    for index in ciphertext_index:
        ciphertext_part += ciphertext[index]
    ciphertext_parts.append(ciphertext_part)
    #print(ciphertext_part.upper())
    #print(f"[{i}] {coincidence_index(ciphertext_part)}")
    i += 1
#print(ciphertext_parts)

plaintext_parts = []
keys = [9, 0, 13, 4, 19]
for i in range(m):
    plaintext_parts.append(shift_text(ciphertext_parts[i], keys[i]))
#print(plaintext_parts)

plaintext = ""
for i in range(ciphertext_length):
    plaintext += plaintext_parts[i % m][int((i - (i % m)) / m)]
print(plaintext)
