"""
floyd算法
问题：找出所有点对的最短路径（有向图无向图均可）
解法：设D(k,i,j)为从vi到vj只使用v1,v2,...,vk作为中间顶点的最短路径的权，则D(k,i,j)的值遵从D(k,i,j) = min{ D(k-1,i,j), D(k-1,i,k) + D(k-1,k,j) }
"""


# 构建领接矩阵（以算法导论图25.1为例）
def build_adjacency_matrix():
    import numpy as np
    return np.array([[0, 3, 8, float('inf'), -4],
                     [float('inf'), 0, float('inf'), 1, 7],
                     [float('inf'), 4, 0, float('inf'), float('inf')],
                     [2, float('inf'), -5, 0, float('inf')],
                     [float('inf'), float('inf'), float('inf'), 6, 0]])


def floyd(matrix):
    length = len(matrix)
    floyd_matrix = matrix.copy()
    for k in range(length):
        for i in range(length):
            for j in range(length):
                if floyd_matrix[i][k] + floyd_matrix[k, j] < floyd_matrix[i][j]:
                    floyd_matrix[i][j] = floyd_matrix[i][k] + floyd_matrix[k, j]
    return floyd_matrix


if __name__ == '__main__':
    adjacency_matrix = build_adjacency_matrix()
    print(adjacency_matrix)
    min_path_matrix = floyd(adjacency_matrix)
    print(min_path_matrix)
