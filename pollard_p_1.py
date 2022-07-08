# -*- coding=UTF-8 -*-
# @File : pollard_p_1.py
# @Author : CanisMinor
# @Date : 2022-07-08

import gmpy2

n = 15770708441
B = 180
a = 2
for i in range(2, B + 1):
    a = gmpy2.powmod(a, i, n)
d = gmpy2.gcd(a - 1, n)
if d > 1 and d < n:
    print(d)
# n=d*s
s = n / d
print(s)