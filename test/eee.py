# -*- coding: utf-8 -*-

from functools import reduce


def str2num(s):
    try:
        ret = int(s)
    except ValueError as e:
        print('Erroe', e)
        raise e
    finally:
        print('finally...')
    return ret


def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)


def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)


main()
