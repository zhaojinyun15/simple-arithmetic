"""
floyd算法
问题：找出所有点对的最短路径（有向图无向图均可）
解法：设D(k,i,j)为从vi到vj只使用v1,v2,...,vk作为中间顶点的最短路径的权，则D(k,i,j)的值遵从D(k,i,j) = min{ D(k-1,i,j), D(k-1,i,k) + D(k-1,k,j) }
"""
import sys

import numpy as np


# 构建领接矩阵（以算法导论图25.1为例）
def build_adjacency_matrix():
    return np.array([[0, 3, 8, float('inf'), -4],
                     [float('inf'), 0, float('inf'), 1, 7],
                     [float('inf'), 4, 0, float('inf'), float('inf')],
                     [2, float('inf'), -5, 0, float('inf')],
                     [float('inf'), float('inf'), float('inf'), 6, 0]])


def floyd(matrix):
    """
    N^3
    :param matrix:
    :return:
    """
    length = len(matrix)
    floyd_matrix = matrix.copy()
    path_matrix = np.zeros(shape=(length, length))
    for k in range(length):
        for i in range(length):
            for j in range(length):
                if floyd_matrix[i][k] + floyd_matrix[k, j] < floyd_matrix[i][j]:
                    floyd_matrix[i][j] = floyd_matrix[i][k] + floyd_matrix[k, j]
                    path_matrix[i][j] = k + 1
    return floyd_matrix, path_matrix


def print_shortest_path(path_matrix, i, j):
    """
    根据路径矩阵，得到从i到j相应的路径
    :param path_matrix:
    :param i:
    :param j:
    :return:
    """
    path_list = []
    search_for_path(path_matrix, i, j, path_list)
    path_list.append(f"v{j}")
    print(' -> '.join(path_list))


def search_for_path(path_matrix, i, j, path_list):
    k = int(path_matrix[i - 1][j - 1])
    if k > 0:
        search_for_path(path_matrix, i, k, path_list)
        search_for_path(path_matrix, k, j, path_list)
    else:
        path_list.append(f"v{i}")


if __name__ == '__main__':
    adjacency_matrix = build_adjacency_matrix()
    print("adjacency_matrix = ")
    print(adjacency_matrix)
    min_value_matrix, min_path_matrix = floyd(adjacency_matrix)
    print("min_value_matrix = ")
    print(min_value_matrix)
    print("min_path_matrix = ")
    print(min_path_matrix)
    print_shortest_path(min_path_matrix, 1, 3)
