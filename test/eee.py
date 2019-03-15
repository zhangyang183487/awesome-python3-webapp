# -*- coding: utf-8 -*-

from functools import reduce


def str2num(s):
    ret = 0
    try:
        ret = int(s)
    except ValueError as e:
        print('Erroe', e);
        raise e;
    finally:
        print('finally...')
    return ret


def calc(exp):
    '''
    
    Function to calc sum of list.

    Example:

    >>> calc('100 + 200 + 345')
    12
    
    '''

    ss = exp.split('+')
    print(ss)
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)


def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)

    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)


main()
