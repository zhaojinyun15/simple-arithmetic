"""
问题：设有一个矩阵序列，做乘积运算，S=ABCDEFG...，每个矩阵的的行列数分别为：A_{c0,c1}, B_{c1,c2}, C_{c2,c3}...，试求出使得乘法运算次数最少的矩阵乘法运算先后顺序即总运算次数。
比如三个矩阵乘积，行列数分别为5*4，4*3，3*2，则先计算前两个后再与第三个相乘的运算量是：5*4*3+5*3*2=90；先计算后两个后再与第一个相乘的运算量是：4*3*2+5*4*2=64。所以先算后两个是这个问题的解。
问题可以抽象成N个矩阵，有N+1个数
"""
import random


def prepare_num_list(num):
    max_num = num * 10
    random_list = []
    for i in range(num + 1):
        random_list.append(random.randint(1, max_num))
    return random_list


def opt_matrix(row_column_list, best_num_matrix, split_index_matrix, left_index, right_index):
    """
    将序列分成两部分，递归地求解每一部分的，同时计算递归得出的两个矩阵的结果，对于所有的分成两部分的情况，取最小值
    :param row_column_list:
    :param best_num_matrix:
    :param split_index_matrix:
    :param left_index:
    :param right_index:
    :return:
    """
    if right_index - left_index < 1:
        raise Exception('index error!')
    if right_index - left_index == 1:
        return
    if best_num_matrix[left_index][right_index] != 0:
        # 说明已经算过这种情况了，直接返回。如果不加这步，会造成大量重复计算，时间复杂度将是指数的。
        return
    split_index = left_index + 1
    min_num = float("inf")
    result_split_index = split_index
    while split_index < right_index:
        opt_matrix(row_column_list, best_num_matrix, split_index_matrix, left_index, split_index)
        opt_matrix(row_column_list, best_num_matrix, split_index_matrix, split_index, right_index)
        tmp_num = best_num_matrix[left_index, split_index] + best_num_matrix[split_index, right_index] + \
                  row_column_list[left_index] * row_column_list[split_index] * row_column_list[right_index]
        if tmp_num < min_num:
            min_num = tmp_num
            result_split_index = split_index
        split_index += 1
    best_num_matrix[left_index][right_index] = min_num
    split_index_matrix[left_index][right_index] = result_split_index


if __name__ == '__main__':
    matrix_num = 10
    x_list = prepare_num_list(matrix_num)
    # matrix_num = 4
    # x_list = [2, 4, 3, 6, 2]
    print(x_list)
    import numpy as np
    result_matrix = np.zeros(shape=(matrix_num + 1, matrix_num + 1))
    split_index_matrix = np.zeros(shape=(matrix_num + 1, matrix_num + 1))
    opt_matrix(x_list, result_matrix, split_index_matrix, 0, matrix_num)
    # print(result_matrix)
    # print(split_index_matrix)
    print(result_matrix[0][matrix_num])
