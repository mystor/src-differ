from __future__ import print_function
import os, sys
from zss import simple_distance, Node

# Import the correct parser
_, ext = os.path.splitext(sys.argv[1])
if ext == '.c':
    from cparse import get_children, get_label, make_tree
elif ext == '.py':
    from pparse import get_children, get_label, make_tree
else:
    print("Unsupported file extension: {}".format(ext))
    sys.exit(1)

def to_dumb_nodes(tree):
    """ Transform ast into zss nodes """
    n = Node(get_label(tree))
    for c in get_children(tree):
        cn = to_dumb_nodes(c)
        n.addkid(cn)
    return n

def compute_distance(file1, file2):
    """ Compute tree distance between two files """
    f1tree = to_dumb_nodes(make_tree(file1))
    f2tree = to_dumb_nodes(make_tree(file2))

    return simple_distance(f1tree, f2tree)

if __name__ == '__main__':
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    distance = compute_distance(file1, file2)
    print("Distance is: {}".format(distance))
