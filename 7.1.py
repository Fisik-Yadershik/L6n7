#!/usr/bin/ env python3
# -*- coding: utf-8 -*-

# Ввести список А из 10 элементов, найти сумму элементов, больших 2 и меньших 20 и #
# кратных 8, их количество и вывести результаты на экран. #

import sys

if __name__ == '__main__':
    A = tuple(map(int, input().split()))
    if len(A) != 10:
        print("Неверный размер списка", file=sys.stderr)
        exit(1)
    s = 0
    k = 0
    for item in A:
        if (item < 20 and item > 2 and item % 8 == 0):
            s += item
            k +=1
    print(s)
    print(k)

