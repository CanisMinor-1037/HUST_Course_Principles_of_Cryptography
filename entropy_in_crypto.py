#!/usr/bin/python3
# @File : entropy_in_crypto.py
# @Author : CanisMinor
# @Date : 2022-07-08

import math

enc = {
    'k1': {
        'a': 1,
        'b': 2
    },
    'k2': {
        'a': 2,
        'b': 3
    },
    'k3': {
        'a': 3,
        'b': 4
    },
}
pr_x_dic = {'a': 1 / 4, 'b': 3 / 4}
pr_k_dic = {'k1': 1 / 2, 'k2': 1 / 4, 'k3': 1 / 4}
pr_y_dic = {1: 0, 2: 0, 3: 0, 4: 0}  #未计算
fit_keys = []

def all_fit_keys(target_x, target_y, enc_dic=enc):
    """y|x下所有合适的k"""
    fit_keys = []
    for k in enc_dic.keys():
        for x, y in enc_dic[k].items():
            if x == target_x and y == target_y:
                fit_keys.append(k)
                break
    return fit_keys

def cal_pr_y_x(target_y, target_x, pr_dic=pr_k_dic):
    """计算Pr[y|x]"""
    fit_keys = all_fit_keys(target_x, target_y)
    pr = 0
    for fit_key in fit_keys:
        pr += pr_dic[fit_key]
    return pr

def cal_pr_y(target_y, pr_dic_1=pr_x_dic, pr_dic_2=pr_k_dic):
    """计算Pr[y]"""
    pr = 0
    for x in pr_dic_1.keys():
        fit_keys = all_fit_keys(x, target_y)
        for fit_key in fit_keys:
            pr += pr_dic_2[fit_key] * pr_dic_1[x]
    return pr

def cal_pr_y_k(target_y, target_k, enc_dic=enc, pr_dic=pr_x_dic):
    """计算Pr[y|k]"""
    if target_y not in enc_dic[target_k].values():
        return 0
    else:
        for x, y in enc_dic[target_k].items():
            if y == target_y:
                return pr_dic[x]

def cal_pr_k_y(target_k, target_y, pr_dic_1=pr_y_dic, pr_dic_2=pr_k_dic):
    """计算Pr[k|y]"""
    pr_y_k = cal_pr_y_k(target_y, target_k)
    pr_k_y = pr_y_k * pr_dic_2[target_k] / pr_dic_1[target_y]
    return pr_k_y

def cal_entropy(pr_dic):
    """计算随机变量的信息熵"""
    entropy = 0
    for value in pr_dic.values():
        if value != 0:
            entropy += (-math.log2(value) * value)
    return entropy

# 结果Pr[Y = y]
for y in pr_y_dic.keys():
    pr_y_dic[y] = cal_pr_y(y)
    print(f"Pr[Y={y}] = {pr_y_dic[y]}")
print('\n')

# Pr[X = x]
for x in pr_x_dic.keys():
    print(f"Pr[X={x}] = {pr_x_dic[x]}")
print('\n')

# 结果Pr[X = x, Y = y]
for y in pr_y_dic.keys():
    for x in pr_x_dic.keys():
        pr_y_x = cal_pr_y_x(y, x)
        # Pr[x|y]
        pr_x_y = pr_y_x * pr_x_dic[x] / pr_y_dic[y]
        print(f"Pr[X={x} | Y={y}] = {pr_x_y}")
    print('\n')
    
h_k_c = 0
for y in pr_y_dic.keys():
    pr_k_y_dic = {}
    for k in pr_k_dic.keys():
        pr_k_y_dic[k] = cal_pr_k_y(k, y)
    #print(pr_k_y_dic)
    h_k_c += cal_entropy(pr_k_y_dic) * pr_y_dic[y]

entropy_x = cal_entropy(pr_x_dic)
entropy_y = cal_entropy(pr_y_dic)
entropy_k = cal_entropy(pr_k_dic)
print(f"H(P) = {entropy_x}")
print(f"H(K) = {entropy_k}")
print(f"H(C) = {entropy_y}")
print(f"H(K)+H(P)-H(C) = {entropy_k+entropy_x-entropy_y}")
print(f"H(K|C) = {h_k_c}")