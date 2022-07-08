#!/usr/bin/python3
# @File : perfect_secrecy.py
# @Author : CanisMinor
# @Date : 2022-07-08

enc = {
    'k1': {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4
    },
    'k2': {
        'a': 2,
        'b': 3,
        'c': 4,
        'd': 5
    },
    'k3': {
        'a': 3,
        'b': 4,
        'c': 5,
        'd': 1
    },
    'k4': {
        'a': 4,
        'b': 5,
        'c': 1,
        'd': 2
    },
    'k5': {
        'a': 5,
        'b': 1,
        'c': 2,
        'd': 3
    },
}

pr_x = {'a': 1 / 2, 'b': 1 / 4, 'c': 1 / 8, 'd': 1 / 8}
pr_k = {'k1': 1 / 5, 'k2': 1 / 5, 'k3': 1 / 5, 'k4': 1 / 5, 'k5': 1 / 5}
pr_y = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}  #未计算
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


def cal_pr_y_x(target_y, target_x, pr_dic=pr_k):
    """计算Pr[y|x]"""
    fit_keys = all_fit_keys(target_x, target_y)
    pr = 0
    for fit_key in fit_keys:
        pr += pr_dic[fit_key]
    return pr


def cal_pr_y(target_y, pr_dic_x=pr_x, pr_dic_k=pr_k):
    """计算Pr[y]"""
    pr = 0
    for x in pr_dic_x.keys():
        fit_keys = all_fit_keys(x, target_y)
        for fit_key in fit_keys:
            pr += pr_dic_k[fit_key] * pr_dic_x[x]
    return pr


# 结果Pr[Y = y]
for y in pr_y.keys():
    pr_y[y] = cal_pr_y(y)
    print(f"Pr[Y={y}] = {pr_y[y]}")
print('\n')

# Pr[X = x]
for x in pr_x.keys():
    print(f"Pr[X={x}] = {pr_x[x]}")
print('\n')

# 结果Pr[X = x, Y = y]
for y in pr_y.keys():
    for x in pr_x.keys():
        pr_y_x = cal_pr_y_x(y, x)
        # Pr[x|y]
        pr_x_y = pr_y_x * pr_x[x] / pr_y[y]
        print(f"Pr[X={x} | Y={y}] = {pr_x_y}")
    print('\n')