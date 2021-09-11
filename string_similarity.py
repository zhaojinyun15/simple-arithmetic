
def levenshtein_distance(str1, str2):
    """
    参考：https://www.cnblogs.com/xiaoyulong/p/8846745.html
    :param str1: 字符串1
    :param str2: 字符串2
    :return: 两个字符串的相似度
    """
    len1 = len(str1)
    len2 = len(str2)
    import numpy as np
    matrix = np.zeros((len1 + 1, len2 + 1))
    for i in range(len1 + 1):
        for j in range(len2 + 1):
            if i == 0:
                m_ij = j
            else:
                if j == 0:
                    m_ij = i
                else:
                    m_ij = min(matrix[i][j - 1] + 1,
                               matrix[i - 1][j] + 1,
                               matrix[i - 1][j - 1] if str1[i - 1] == str2[j - 1] else matrix[i - 1][j - 1] + 1)
            matrix[i][j] = m_ij
    return 1 - matrix[len1][len2] / max(len1, len2)


if __name__ == '__main__':
    similarity = levenshtein_distance("afghggfds", "ghngvbhn")
    print(similarity)
