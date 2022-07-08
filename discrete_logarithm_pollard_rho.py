# -*- coding=UTF-8 -*-
# @File : discrete_logarithm_pollard_rho.py
# @Author : CanisMinor
# @Date : 2022-07-08

import gmpy2

p = 809
alpha = 89
beta = 618
n = 101

def f(args, alpha=alpha, beta=beta):
    results = [0, 0, 0]
    switch_x = args[0] % 3
    if switch_x == 1:
        results[0] = gmpy2.powmod(beta * args[0], 1, p)
        results[1] = gmpy2.powmod(args[1], 1, n)
        results[2] = gmpy2.powmod(args[2] + 1, 1, n)
    elif switch_x == 0:
        results[0] = gmpy2.powmod(args[0], 2, p)
        results[1] = gmpy2.powmod(2 * args[1], 1, n)
        results[2] = gmpy2.powmod(2 * args[2], 1, n)
    else:
        results[0] = gmpy2.powmod(alpha * args[0], 1, p)
        results[1] = gmpy2.powmod(args[1] + 1, 1, n)
        results[2] = gmpy2.powmod(args[2], 1, n)
    return results

x_list = f([1, 0, 0])
y_list = f(x_list)
print("{}\t{}").format(x_list, y_list)
while x_list[0] != y_list[0]:
    x_list = f(x_list)
    y_list = f(y_list)
    y_list = f(y_list)
    print("{}\t{}").format(x_list, y_list)
if gmpy2.gcd(x_list[2] - y_list[2], n) == 1:
    temp = gmpy2.powmod(y_list[2] - x_list[2], -1, n)
    ind = gmpy2.powmod((x_list[1] - y_list[1]) * temp, 1, n)
    print(ind)