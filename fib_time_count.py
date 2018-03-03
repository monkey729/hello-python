# -*- coding:utf-8 -*-
dict_num = {}
new_num = {}

#找规律
def f(n):
    if n == 1:
        return 2
    if n == 2:
        return 3
    if n > 2:
        return f(n - 1) * 2
        
#生成规律字典
def func(num):
    count = 0
    for i in range(1, num + 1):
        global dict_num
        dict_num[i] = f(i)
        count = count + dict_num[i]
        if count >= num:
            break

    for k, v in dict_num.items():
        global new_num
        if k == 1:
            new_num[k] = [1, 2]
        if k > 1:
            s = 0
            for i in range(1, k + 1):
                s = s + f(i)
            new_num[k] = [(new_num[k - 1][1] + 1), s]
        if new_num[k][1] >= num:
            break


def find_num(n):
    global new_num
    for k, v in new_num.items():
        li = []
        li.append(v)
        for i in range(li[0][0], li[0][1] + 1):
            if i == n:
                return k


while True:
    num = int(input("输入一个数："))
    func(num)
    #print(dict_num)
    #print(new_num)
    print(find_num(num))
