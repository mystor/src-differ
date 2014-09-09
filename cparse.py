from __future__ import print_function
from clang.cindex import Index, Config
import sys

# Ugly hack because mac os x :'(
if sys.platform == "darwin":
    Config.set_library_path("/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/lib/")

def get_children(node):
    return node.get_children()

def get_label(node):
    return str(node.kind)

def make_tree(fname):
    idx = Index.create()
    return idx.parse(fname).cursor
