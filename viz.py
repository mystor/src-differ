from __future__ import print_function
import os, sys
from graphviz import Digraph

# Import the correct parser
_, ext = os.path.splitext(sys.argv[1])
if ext == '.c':
    from cparse import get_children, get_label, make_tree
elif ext == '.py':
    from pparse import get_children, get_label, make_tree
else:
    print("Unsupported file extension: {}".format(ext))
    sys.exit(1)

counter = 0
dot = Digraph()

def visit(node):
    """ Add the node and its children to the digraph dot """
    global counter
    parent_id = counter
    dot.node(str(parent_id), get_label(node))
    counter = counter + 1

    for child in get_children(node):
        child_id = visit(child)
        dot.edge(str(parent_id), str(child_id))

    return parent_id

if __name__ == '__main__':
    visit(make_tree(sys.argv[1]))
    dot.render('viz', view=True)
