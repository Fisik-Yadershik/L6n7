#!/usr/bin/ env python3
# -*- coding: utf-8 -*-

# В списке, состоящем из вещественных элементов, вычислить: #
# 1) количество элементов списка, равных 0; #
# 2) сумму элементов списка, расположенных после минимального элемента. #
# Упорядочить элементы списка по возрастанию модулей элементов. #

import sys

if __name__ == '__main__':
    A = list(map(int, input().split()))
    k = 0
    for item in A:
        if (item == 0):
            k +=1
    mn = A.index(min(A))
    l = sum(A[mn:])
    A.sort()
    print(k)
    print(l)
    print(A)

