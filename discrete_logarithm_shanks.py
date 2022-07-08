# -*- coding=UTF-8 -*-
# @File : discrete_logarithm_shanks.py
# @Author : CanisMinor
# @Date : 2022-07-08
# -*- coding=UTF-8 -*-
import math
import gmpy2

n = 808
G = range(1, 809)
a = 3
b = 525

m = int(math.sqrt(n)) + 1
#print(m)
L1 = {}
for j in range(m):
    L1[j] = gmpy2.powmod(a, m * j, n + 1)
sorted_L1 = sorted(L1.items(), key=lambda item: item[1], reverse=False)

L2 = {}
for i in range(m):
    temp = gmpy2.powmod(a, -i, n + 1)
    L2[i] = gmpy2.powmod(temp * b, 1, n + 1)
sorted_L2 = sorted(L2.items(), key=lambda item: item[1], reverse=False)

print(sorted_L1)
print(sorted_L2)
for e_L1 in sorted_L1:
    for e_L2 in sorted_L2:
        if e_L1[1] == e_L2[1]:
            j = e_L1[0]
            i = e_L2[0]
        elif e_L1[1] < e_L2[1]:
            break

print((m * j + i) % n)
