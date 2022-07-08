# -*- coding=UTF-8 -*-
# @File : pollard_rho.py
# @Author : CanisMinor
# @Date : 2022-07-08

import gmpy2
def f(x, n):
    return (x**2 + 1) % n

n = 7171
x = 1
y = f(x, n)
p = gmpy2.gcd(x - y, n)
while p == 1:
    x = f(x, n)
    y = f(f(y, n), n)
    p = gmpy2.gcd(x - y, n)
if p != n:
    print(p)
    # n = p*s
    s = n / p
    print(s)