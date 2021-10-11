"""
素数检测算法
"""
import math
import random


def factor_traversal(num):
    """
    N^(1/2)
    :param num:
    :return:
    """
    square_root = math.sqrt(num)
    for i in range(2, int(square_root) + 1):
        if num % i == 0:
            return False
    return True


def miller_rabin(num):
    """
    klogN
    :param num:
    :return:
    """
    if not isinstance(num, int):
        raise Exception('not an int')
    if num < 2:
        raise Exception('num < 2')
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    # 多次检测
    for i in range(100):
        if not miller_rabin_prime_test(num):
            return False
    return True


def miller_rabin_prime_test(num):
    a = random.randint(2, num - 1)
    s = 0
    d = num - 1
    while d % 2 == 0:
        s += 1
        d >>= 1
    x = quick_power(a, d, num)
    for i in range(s):
        new_x = quick_power(x, 2, num)
        if new_x == 1 and x != 1 and x != num - 1:
            return False
        x = new_x
    if x != 1:
        return False
    return True


def quick_power(a, b, c):
    result = 1
    while b > 0:
        if b % 2 == 1:
            result = result * a % c
        a = a * a % c
        b >>= 1
    return result


if __name__ == '__main__':
    print(miller_rabin(2 ** 400 - 593))

    # print(factor_traversal(101))
    # print(miller_rabin(101))
    # print(quick_power(326, 3560, 17))
