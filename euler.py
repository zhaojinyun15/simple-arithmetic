"""
问题：欧拉问题，判断图是否可以一笔画，如果可以，给出一个路径
思路：图满足全是偶点（可从任一点出发，并回到出发点），或只有两个奇点，其余全是偶点的（从某一奇点出发，并回到另一奇点）才能一笔画，前一种叫Euler circuit，后一种叫Euler tour
注意：由于图比较稀疏，所以采用只列出边的形式，若是无向图，所以每个边都只表示一次
"""

import random

# 书上例子，p274
euler_list_1 = [
    (1, 3),
    (1, 4),
    (2, 3),
    (2, 8),
    (8, 9),
    (3, 6),
    (3, 9),
    (6, 9),
    (3, 4),
    (3, 7),
    (7, 9),
    (4, 7),
    (4, 10),
    (7, 10),
    (9, 10),
    (9, 12),
    (10, 12),
    (4, 5),
    (5, 10),
    (4, 11),
    (10, 11),
    # (5, 11),
]


def add_to_dict(result_dict, element):
    if result_dict.get(element) is None:
        result_dict[element] = 1
    else:
        result_dict[element] += 1


def check_odd_even(edge_list):
    odd_num = 0
    odd_points = set()
    all_points = set()
    for edge in edge_list:
        for point in edge:
            all_points.add(point)
            if point not in odd_points:
                odd_num += 1
                odd_points.add(point)
            else:
                odd_num -= 1
                odd_points.remove(point)
    if odd_num == 0:
        print('---------Euler circuit---------')
        return all_points
    elif odd_num == 2:
        print('---------Euler tour---------')
        return odd_points
    else:
        print('---------no solution---------')
        return None


def dfs(start_point, edge_status, path):
    for edge in edge_status.keys():
        if edge_status[edge] and start_point in edge:
            edge_status[edge] = False
            dfs(edge[0] if edge[1] == start_point else edge[1], edge_status, path)
    path.insert(0, start_point)


def solve_euler_problem(edge_list):
    start_points = check_odd_even(edge_list)
    if start_points is None:
        return
    # 选一个开始点
    start_point = random.choice(list(start_points))
    # start_point = 5
    print(f'{start_point=}')
    edge_status = dict(zip(edge_list, [True] * len(edge_list)))
    path = []
    dfs(start_point, edge_status, path)
    print(path)


if __name__ == '__main__':
    solve_euler_problem(euler_list_1)
