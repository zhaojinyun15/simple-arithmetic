"""
问题：有凹凸的地面（用一个数组/多维数组表示，里面的值代表凸起的高度），形成的水坑，总共能容纳多少水
"""
import random


def one_dimension():
    length = 15
    min_height = 0
    max_height = 10
    puddle = build_one_dimension_puddle_by_random(length, min_height, max_height)
    print(f'puddle array is {puddle}')
    v = calculate_one_dimension_puddle(puddle, 0, length - 1)
    print(f'The volume of puddle is {v}')


def build_one_dimension_puddle_by_random(length, min_height, max_height):
    puddle = []
    for _ in range(length):
        puddle.append(random.randint(min_height, max_height))
    return puddle


def calculate_one_dimension_puddle(puddle, left_index, right_index):
    if left_index >= right_index:
        return 0
    v = 0
    left_height = puddle[left_index]
    right_height = puddle[right_index]
    if left_height < right_height:
        i = left_index + 1
        while i < right_index:
            i_height = puddle[i]
            if i_height <= left_height:
                v += (left_height - i_height)
            else:
                v += calculate_one_dimension_puddle(puddle, i, right_index)
                break
            i += 1
    else:
        i = right_index - 1
        while i > left_index:
            i_height = puddle[i]
            if i_height <= right_height:
                v += (right_height - i_height)
            else:
                v += calculate_one_dimension_puddle(puddle, left_index, i)
                break
            i -= 1
    return v


if __name__ == '__main__':
    # print(build_one_dimension_puddle_by_random(10, 2, 15))
    one_dimension()
