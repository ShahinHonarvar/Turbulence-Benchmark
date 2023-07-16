import ast
from anytree import Node, RenderTree


def create_tree(node, parent):
    ast_node = Node(str(node.__class__.__name__), parent=parent)
    for child in ast.iter_child_nodes(node):
        create_tree(child, ast_node)


with open('g.txt', 'r') as f:
    code = f.read()

tree = ast.parse(code)
root = Node("Root")
create_tree(tree, root)

with open('tree.txt', "w") as f:
    for x, _, node in RenderTree(root):
        f.write("%s%s\n" % (x, node.name))
