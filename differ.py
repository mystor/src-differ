from __future__ import print_function
import os, sys
from zss import simple_distance, Node

def diff(file1, file2):
    # Import the correct parser
    _, ext = os.path.splitext(file1)
    _, ext2 = os.path.splitext(file2)
    if ext != ext2:
        raise NotImplementedError("Different file extensions: {}, {}".format(ext, ext2))

    if ext == '.c':
        from cparse import get_children, get_label, make_tree
    elif ext == '.py':
        from pparse import get_children, get_label, make_tree
    else:
        raise NotImplementedError("Unsupported file extension: {}".format(ext))

    def to_dumb_nodes(tree):
        """ Transform ast into zss nodes """
        n = Node(get_label(tree))
        for c in get_children(tree):
            cn = to_dumb_nodes(c)
            n.addkid(cn)
        return n

    """ Compute tree distance between two files """
    f1tree = to_dumb_nodes(make_tree(file1))
    f2tree = to_dumb_nodes(make_tree(file2))

    return simple_distance(f1tree, f2tree)

if __name__ == '__main__':
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    distance = diff(file1, file2)
    print("Distance is: {}".format(distance))
