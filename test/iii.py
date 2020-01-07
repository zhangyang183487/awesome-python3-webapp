#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def find_solution(n):
    if n is None or n <= 0:
        return

    temp = n

    i = 0

    if temp >= 10:
        i = (temp - temp % 10) / 10
        temp = temp - 10 * i

    j = 0
    if temp >= 5:
        j = (temp - temp % 5) / 5
        temp = temp - 5 * j

    k = 0
    if temp >= 2:
        k = (temp - temp % 2) / 2
        temp = temp - 2 * k

    if temp == 0:
        print('需要%d张10元，%d张5元，%d张2元，刚好凑齐%d' % (i, j, k, n))
    else:
        print('不能刚好凑齐%d' % n)


def find_solution_2(n):
    if n is None or n <= 0:
        return

    temp = n

    i = temp // 10
    temp = temp % 10

    j = temp // 5
    temp = temp % 5

    k = temp // 2
    temp = temp % 2

    if temp == 0:
        print('需要%d张10元，%d张5元，%d张2元，刚好凑齐%d' % (i, j, k, n))
    else:
        print('不能刚好凑齐%d' % n)


if __name__ == "__main__":
    find_solution_2(7)
