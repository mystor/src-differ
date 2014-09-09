from sys import argv
from zss import simple_distance, Node
from cparse import get_children, get_label, make_tree

def label_distance(l1, l2):
    if l1 == l2:
        return 0
    else:
        return 1

def to_dumb_nodes(tree):
    n = Node(get_label(tree))
    for c in get_children(tree):
        cn = to_dumb_nodes(c)
        n.addkid(cn)
    return n

def compute_distance(file1, file2):
    # Parse the two c files
    f1tree = to_dumb_nodes(make_tree(file1))
    f2tree = to_dumb_nodes(make_tree(file2))

    # Compute the tree edit distance between the trees
    distance = simple_distance(
        f1tree,
        f2tree,
    )

    return distance

if __name__ == '__main__':
    file1 = argv[1]
    file2 = argv[2]
    distance = compute_distance(file1, file2)
    print("Distance is: {}".format(distance))
