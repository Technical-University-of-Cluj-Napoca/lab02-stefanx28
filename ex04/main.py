import sys
from BST import BST
from search_engine import search_loop

if __name__ == "__main__":

    source = sys.argv[1]
    opts = {}
    if '--url' in sys.argv:
        opts['url'] = True
    else:
        opts['file'] = True
    tree = BST(source, **opts)
    search_loop(tree)