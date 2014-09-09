import ast

def get_children(node):
    return list(ast.iter_child_nodes(node))

def get_label(node):
    return node.__class__.__name__

def make_tree(fname):
    with open(fname, 'r') as f:
        return ast.parse(f.read(), fname)
