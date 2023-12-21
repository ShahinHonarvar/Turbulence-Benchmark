import ast
from graphviz import Source, Digraph

with open('f.txt', 'r') as f, open('h.txt', 'r') as h, open('g.txt', 'r') as g:
    code1 = f.read()
    code2 = h.read()
    code3 = g.read()
tree1 = ast.parse(code1)
tree2 = ast.parse(code3)


def create_graph(node, graph):
    node_name = str(node.__class__.__name__)

    # colours available at https://graphviz.org/doc/info/colors.html
    graph.node(str(node), label=node_name, style='filled', fillcolor='aquamarine3')
    for child in ast.iter_child_nodes(node):
        child_name = str(child.__class__.__name__)
        graph.node(str(child), label=child_name)
        graph.edge(str(node), str(child))
        create_graph(child, graph)


graph = Digraph()
create_graph(tree2, graph)
src = Source(graph.source)
src.render('tree', view=True)
