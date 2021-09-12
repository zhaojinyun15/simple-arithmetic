"""
问题：平面上有N个点，求距离最近的两个点，以及最短距离。
"""
import math
import random
import time

import numpy


def generate_point(bound, dimension):
    # 方便期间，使生成的点都是非负数，且保留2位小数
    return numpy.array([round(random.uniform(0, bound), 2) for _ in range(dimension)])


def check_point(point, point_set):
    for i in point_set:
        if numpy.array_equal(point, i):
            return True
    return False


def generate_point_set(point_num, bound=1, dimension=2):
    result_list = []
    i = 0
    while i < point_num:
        point = generate_point(bound, dimension)
        if not check_point(point, result_list):
            result_list.append(point)
            i += 1
    return result_list


def get_distance(point_1, point_2):
    dim1 = len(point_1)
    dim2 = len(point_2)
    if dim1 != dim2:
        raise Exception('distance error, dimension of point_1 not equal to dimension of point_2')
    distance = 0
    for i in range(dim1):
        distance += (point_1[i] - point_2[i]) ** 2
    return math.sqrt(distance)


def solved_by_enum_all_point_pair(point_set):
    """
    N^2
    :param point_set:
    :return:
    """
    point_pair = None
    nearest_distance = float('inf')
    for i in range(len(point_set)):
        p1 = point_set[i]
        j = i + 1
        while j < len(point_set):
            p2 = point_set[j]
            distance = get_distance(p1, p2)
            if distance < nearest_distance:
                nearest_distance = distance
                point_pair = (p1, p2)
            j += 1
    return point_pair, nearest_distance


def divide_and_conquer(x_sort_point_set, y_sort_point_set, left_index, right_index):
    if right_index - left_index == 1:
        left_point = x_sort_point_set[left_index]
        right_point = x_sort_point_set[right_index]
        return (left_point, right_point), get_distance(left_point, right_point)
    mid_index = (right_index + left_index) // 2
    left_result = divide_and_conquer(x_sort_point_set, y_sort_point_set, left_index, mid_index)
    right_result = divide_and_conquer(x_sort_point_set, y_sort_point_set, mid_index, right_index)
    if left_result[1] < right_result[1]:
        point_pair = left_result[0]
        d = left_result[1]
    else:
        point_pair = right_result[0]
        d = right_result[1]
    mid_point = x_sort_point_set[mid_index]
    left_bound = mid_point[0] - d
    right_bound = mid_point[0] + d
    delta_point_set = [point for point in y_sort_point_set if (left_bound < point[0] < right_bound)
                       and not numpy.array_equal(point, mid_point)]
    # 这种算法会存在重复计算
    #
    # 一个是此处对y_sort_point_set做筛选的时候，没有确保选中的点在x_sort_point_set的left_index到right_index范围内（可以再做一次校验，但是这样就没法保证线性时间复杂度了），
    #
    # 还有一点是下面的遍历，并没有保证计算的距离的两点分别在mid_index的两侧，只是单纯的按y轴递增遍历，在同侧的话，两边的递归里已经包含了。
    # 但是下面if p2[1] - p1[1] >= d的校验保证了，该二重循环不会是N^2，而是线性的（最多是7N），
    # 因为在mid_index左边d*d的正方形区域内，最多只能有4个点（分别放在4个角落），否则他们之间的最短距离必然小于d，这与d是左右两边递归得出的最短距离矛盾，右半边的d*d区域同理，故加起来2d*d的区域内最多只会有8个点
    for i in range(len(delta_point_set)):
        p1 = delta_point_set[i]
        j = i + 1
        while j < len(delta_point_set):
            p2 = delta_point_set[j]
            if p2[1] - p1[1] >= d:
                break
            distance = get_distance(p1, p2)
            if distance < d:
                d = distance
                point_pair = (p1, p2)
            j += 1
    return point_pair, d


def solved_by_divide_and_conquer(point_set):
    """
    NlogN
    :param point_set:
    :return:
    """
    x_sort_point_set = sorted(point_set, key=lambda p: p[0])
    y_sort_point_set = sorted(point_set, key=lambda p: p[1])
    return divide_and_conquer(x_sort_point_set, y_sort_point_set, 0, len(point_set) - 1)


if __name__ == '__main__':
    # point_set = generate_point_set(10, 10)
    # print(f'{point_set=}')
    # print(f'{len(point_set[0])=}')
    # print(f'{point[1]=}')
    # p1 = numpy.array([3, 3])
    # p2 = numpy.array([4, 7])
    # print(get_distance(p1, p2))

    point_set = generate_point_set(10000, 20000)
    # print(point_set)

    print('#-' * 40)

    start_time = time.time()
    solution = solved_by_enum_all_point_pair(point_set)
    end_time = time.time()
    print(f'takes time: {(end_time - start_time) * 1000} ms')
    point_pair = solution[0]
    nearest_distance = solution[1]
    print(f'{point_pair=}')
    print(f'{nearest_distance=}')

    print('#-' * 40)

    start_time = time.time()
    solution = solved_by_divide_and_conquer(point_set)
    end_time = time.time()
    print(f'takes time: {(end_time - start_time) * 1000} ms')
    point_pair = solution[0]
    nearest_distance = solution[1]
    print(f'{point_pair=}')
    print(f'{nearest_distance=}')

