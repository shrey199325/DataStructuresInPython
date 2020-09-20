import heapq as H
from typing import List, Any


class Node:
    def __init__(self, val):
        self.val = val
        self.ht = 0
        self.children = []

    def __str__(self):
        return "Node: {}, Ht: {}, children: {}".format(self.val, self.ht, self.children)

    def __repr__(self):
        return "Node: {}, Ht: {}, children: {}".format(self.val, self.ht, self.children)

    def set_ht(self, ht=0):
        self.ht = ht
        for child in self.children:
            child.set_ht(ht+1)


def count_nodes(node: Node) -> int:
    if not node.children:
        return 1
    return 1 + sum([count_nodes(n) for n in node.children])

def ht_creator(node, ht=None, h=0):
    if not ht:
        ht = [0]*count_nodes(node)
    if not node.children:
        ht[node.val] = h
        return ht
    ht[node.val] = h
    for n in node.children:
        ht = ht_creator(n, ht, h+1)
    return ht


def get_parent(root: Node, parent_list: List[int], parent: int=-1) -> List[int]:
    if parent == -1:
        # root condition
        n = count_nodes(root)
        parent_list = [-1] * n
    else:
        parent_list[root.val] = parent
    for child in root.children:
        parent_list = get_parent(child, parent_list, root.val)
    return parent_list


def sparse_table(parent: List[int]) -> List[List[int]]:
    n = len(parent)
    dp = [[0 for _ in range(n + 1)] for __ in range(21)]
    for i in range(21):
        for j in range(n):
            if i == 0:
                dp[i][j] = parent[j]
            else:
                dp[i][j] = dp[i-1][dp[i-1][j]] if dp[i-1][j] >= 0 else -1
    return dp


def lca(st: List[List[int]]) -> int:
    pass

"""
     1
   2 3 4
 5 6    7 8
"""
head = Node(0)
temp = head
temp.children.append(Node(1))
temp.children.append(Node(2))
temp = temp.children[0]
temp.children.append(Node(3))
temp.children.append(Node(4))
temp = head.children[1]
temp.children.append(Node(5))
temp.children.append(Node(6))
temp.children.append(Node(7))
temp = head.children[1].children[1].children.append(Node(8))
head.set_ht()
print(head)
parent_list = []
parent_list = get_parent(head, parent_list)
print(parent_list)
ST = sparse_table(parent_list)
print(ST)
height = ht_creator(head)
print(height)