class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []
        self.count = 0

    def add_child(self, obj):
        self.children.append(obj)
        self.count += 1

    def __str__(self):
        return "Node: {}, children: {}".format(self.data, self.children)

    def __repr__(self):
        return "Node: {}, children: {}".format(self.data, self.children)

n = Node(5)
for i in range(10, 20, 2):
    p = Node(i)
    q = Node(i+1)
    n.add_child(p)
    n.add_child(q)
print(n)