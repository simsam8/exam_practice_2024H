from collections import namedtuple

Node = namedtuple("Node", "label weight children")
Tree = namedtuple("Tree", "n root")


def postfix(tree):
    for child in tree.root.children:
        child_tree = Tree(tree.n + 1, child)
        yield from postfix(child_tree)

    yield tree.root


def wis(tree):
    pass


node5 = Node("node5", 6, [])
node6 = Node("node6", 10, [])
node7 = Node("node7", 8, [])

node3 = Node("node3", 5, [node7])
node4 = Node("node4", 1, [node5, node6])
node1 = Node("node1", 3, [node3])
node2 = Node("node2", 6, [node4])

root = Node("root", 6, [node1, node2])
tree = Tree(0, root)

for node in postfix(tree):
    print(node.label)
