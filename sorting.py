# -*- coding: utf-8 -*-
"""
Сортировки для основного проекта (вариант 14, «complex»).
"""
from copy import copy


def bubble_sort(items):
    """
    Сортировка пузырьком по возрастанию, возвращает новый список
    (исходный не меняет).
    """
    a = copy(list(items))
    n = len(a)
    for i in range(n):
        for j in range(0, n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a
