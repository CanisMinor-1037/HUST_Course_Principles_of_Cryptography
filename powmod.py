# -*- coding=UTF-8 -*-
# @File : powmod.py
# @Author : CanisMinor
# @Date : 2022-07-08

from gmpy2 import powmod
from random import randint

def square_multiply(a, b, n):
    """平方-乘算法计算powmod(a,b,n)"""
    b = bin(b)[2:]
    l = len(b)
    z = 1
    for i in range(l):
        z = powmod(z, 2, n)
        if b[i] == '1':
            z = powmod(z * a, 1, n)
    return z