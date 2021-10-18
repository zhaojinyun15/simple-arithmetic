"""
树相关的算法
"""
import sys


class BinaryTree:
    """
    二叉树
    """
    def __init__(self, root_node):
        self._element = root_node
        self._left_child = None
        self._right_child = None

    def insert_left_child(self, new_node):
        # if self.left_child is not None:
        #     raise Exception('already has left child!')
        if isinstance(new_node, BinaryTree):
            self._left_child = new_node
        else:
            self._left_child = BinaryTree(new_node)

    def insert_right_child(self, new_node):
        # if self.right_child is not None:
        #     raise Exception('already has right child!')
        if isinstance(new_node, BinaryTree):
            self._right_child = new_node
        else:
            self._right_child = BinaryTree(new_node)

    def get_left_child(self):
        return self._left_child

    def get_right_child(self):
        return self._right_child

    def get_element(self):
        return self._element

    def set_element(self, new_node):
        self._element = new_node


def build_a_binary_tree():
    node1 = BinaryTree(1)
    node2 = BinaryTree(2)
    node3 = BinaryTree(3)
    node4 = BinaryTree(4)
    node5 = BinaryTree(5)
    node6 = BinaryTree(6)
    node7 = BinaryTree(7)
    node8 = BinaryTree(8)
    node1.insert_left_child(node2)
    node1.insert_right_child(node3)
    node2.insert_left_child(node4)
    node2.insert_right_child(node5)
    node3.insert_right_child(node6)
    node5.insert_left_child(node7)
    node5.insert_right_child(node8)
    return node1


def pre_order_traversal(tree):
    """
    先序遍历：
    根结点 ---> 左子树 ---> 右子树
    :param tree:
    :return:
    """
    left_child = tree.get_left_child()
    right_child = tree.get_right_child()
    sys.stdout.write(f'{tree.get_element()}  ')
    if left_child is not None:
        pre_order_traversal(left_child)
    if right_child is not None:
        pre_order_traversal(right_child)


def in_order_traversal(tree):
    """
    中序遍历：
    左子树 ---> 根结点 ---> 右子树
    :param tree:
    :return:
    """
    left_child = tree.get_left_child()
    right_child = tree.get_right_child()
    if left_child is not None:
        in_order_traversal(left_child)
    sys.stdout.write(f'{tree.get_element()}  ')
    if right_child is not None:
        in_order_traversal(right_child)


def post_order_traversal(tree):
    """
    后序遍历：
    左子树 ---> 右子树 ---> 根结点
    :param tree:
    :return:
    """
    left_child = tree.get_left_child()
    right_child = tree.get_right_child()
    if left_child is not None:
        post_order_traversal(left_child)
    if right_child is not None:
        post_order_traversal(right_child)
    sys.stdout.write(f'{tree.get_element()}  ')


def level_traversal(tree):
    """
    广度优先，按层级遍历
    :param tree:
    :return:
    """
    queue = [tree]
    while len(queue) > 0:
        node = queue.pop(0)
        sys.stdout.write(f'{node.get_element()}  ')
        left_child = node.get_left_child()
        right_child = node.get_right_child()
        if left_child is not None:
            queue.append(left_child)
        if right_child is not None:
            queue.append(right_child)


if __name__ == '__main__':
    my_tree = build_a_binary_tree()
    pre_order_traversal(my_tree)
    print()
    in_order_traversal(my_tree)
    print()
    post_order_traversal(my_tree)
    print()
    level_traversal(my_tree)
    print()
