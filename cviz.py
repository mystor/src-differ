from graphviz import Digraph
from cparse import get_children, get_label, make_tree
import sys

counter = 0

dot = Digraph()

def visit(node):
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
    print dot
    dot.render('viz', view=True)
