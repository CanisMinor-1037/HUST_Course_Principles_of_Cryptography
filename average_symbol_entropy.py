#!/usr/bin/python3
# @File : average_symbol_entropy.py
# @Author : CanisMinor
# @Date : 2022-07-08

import random
import string
import math

length = int(input("请输入初始随机字符串的长度: "))
random_str = ""
for i in range(length):
    random_str += random.choice(string.ascii_lowercase)
#print(random_str)
m = int(input("请选择分组长度m: "))
# 填充
padding_length = m - length % m
for i in range(padding_length):
    random_str += random.choice(string.ascii_lowercase)
    length += 1
print(f"随机字符串为: {random_str}")
print(f"字符串长度: {length}")
# 分块
block_number = length - m + 1
str_blocks = []
for base in range(block_number):
    str_blocks.append(random_str[base:base + m])
# print(str_blocks)
# 统计频率
str_blocks_frequency = {}
for str_block in str_blocks:
    str_blocks_frequency[str_block] = str_blocks.count(
        str_block) / block_number
# print(str_blocks_frequency)
# 计算熵
entropy = 0
for value in str_blocks_frequency.values():
    entropy += (-math.log2(value) * value)
print(f"平均符号熵为: {entropy/m}")