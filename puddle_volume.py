"""
问题：有凹凸的地面（用一个数组/多维数组表示，里面的值代表凸起的高度），形成的水坑，总共能容纳多少水
"""
import queue
import random


def one_dimension():
    length = 15
    min_height = 0
    max_height = 10
    puddle = build_one_dimension_puddle_by_random(length, min_height, max_height)
    print(f'puddle array is {puddle}')
    v = calculate_one_dimension_puddle(puddle, 0, length - 1)
    print(f'The volume of puddle is {v}')


def two_dimension():
    row_number = 5
    column_number = 5
    min_height = 0
    max_height = 10
    puddle = build_two_dimension_puddle_by_random(row_number, column_number, min_height, max_height)
    print(f'puddle array is {puddle}')
    v = calculate_two_dimension_puddle(puddle)
    print(f'The volume of puddle is {v}')


def build_one_dimension_puddle_by_random(length, min_height, max_height):
    puddle = []
    for _ in range(length):
        puddle.append(random.randint(min_height, max_height))
    return puddle


def build_two_dimension_puddle_by_random(row_number, column_number, min_height, max_height):
    row = []
    for _ in range(row_number):
        column = []
        for _ in range(column_number):
            column.append(random.randint(min_height, max_height))
        row.append(column)
    return row


def calculate_one_dimension_puddle(puddle, left_index, right_index):
    """
    时间复杂度N
    :param puddle:
    :param left_index:
    :param right_index:
    :return:
    """
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


def calculate_two_dimension_puddle(puddle):
    """
    https://www.bilibili.com/video/BV1De4y1v7tr/?p=89&spm_id_from=333.880.my_history.page.click&vd_source=2a549a17ac2ce11328f90dcaaa5ec071
    构建一个优先队列（以高度小为优先），设置一个从优先队列弹出值的最大值变量。
    首先把边界点放入优先队列，然后弹出最小的元素，计算最小元素与最大值变量的差作为这个格点的蓄水量，同时更新最大值变量，并将四周为进过队列的格点放入优先队列，循环以上操作，直到队列里的所有元素都弹出。
    时间复杂度：N，N为所有格点的数量 = row_number * column_number
    :param puddle:
    :return:
    """
    row_number = len(puddle)
    column_number = len(puddle[0])
    heap = queue.PriorityQueue()
    # prepare a matrix to show whether the point has been put into heap
    is_enable = [[0] * column_number for _ in range(row_number)]
    # put the edge point of puddle to heap
    for c in range(column_number):
        heap.put((puddle[0][c], 0, c))
        is_enable[0][c] = 1
        heap.put((puddle[row_number - 1][c], row_number - 1, c))
        is_enable[row_number - 1][c] = 1
    for r in range(1, row_number - 1):
        heap.put((puddle[r][0], r, 0))
        is_enable[r][0] = 1
        heap.put((puddle[r][column_number - 1], r, column_number - 1))
        is_enable[r][column_number - 1] = 1

    # calculate
    water = 0
    m = 0
    while not heap.empty():
        p = heap.get()
        height = p[0]
        r = p[1]
        c = p[2]
        water += max(0, m - height)
        m = max(m, height)
        # put the neighbor point into heap
        if r - 1 >= 0 and is_enable[r - 1][c] == 0:
            heap.put((puddle[r - 1][c], r - 1, c))
            is_enable[r - 1][c] = 1
        if r + 1 < row_number and is_enable[r + 1][c] == 0:
            heap.put((puddle[r + 1][c], r + 1, c))
            is_enable[r + 1][c] = 1
        if c - 1 >= 0 and is_enable[r][c - 1] == 0:
            heap.put((puddle[r][c - 1], r, c - 1))
            is_enable[r][c - 1] = 1
        if c + 1 < column_number and is_enable[r][c + 1] == 0:
            heap.put((puddle[r][c + 1], r, c + 1))
            is_enable[r][c + 1] = 1
    return water


if __name__ == '__main__':
    # print(build_one_dimension_puddle_by_random(10, 2, 15))
    # one_dimension()
    two_dimension()
