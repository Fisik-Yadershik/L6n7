#!/usr/bin/ env python3
# -*- coding: utf-8 -*-

# В списке, состоящем из вещественных элементов, вычислить: #
# 1) количество элементов списка, равных 0; #
# 2) сумму элементов списка, расположенных после минимального элемента. #
# Упорядочить элементы списка по возрастанию модулей элементов. #

import sys

if __name__ == '__main__':
    A = tuple(map(int, input().split()))
    k = A.count(0)
    mn = A.index(min(A))
    l = sum(A[mn:])
    B = tuple(sorted(A))
    print(k)
    print(l)
    print(B)

