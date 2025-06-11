'''
Завдання 5. Візуалізація обходу бінарного дерева

Використовуючи код із завдання 4 для побудови бінарного дерева, необхідно створити програму на Python, яка візуалізує обходи дерева: у глибину та в ширину.

Вона повинна відображати кожен крок у вузлах з різними кольорами, використовуючи 16-систему RGB (приклад #1296F0). Кольори вузлів мають змінюватися від темних до світлих відтінків, залежно від послідовності обходу. Кожен вузол при його відвідуванні має отримувати унікальний колір, який візуально відображає порядок обходу.

👉🏻 Примітка. Використовуйте стек та чергу, НЕ рекурсію
'''


import matplotlib.pyplot as plt
import networkx as nx
import uuid
from collections import deque
import colorsys

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.color = "#cccccc"  # default grey
        self.id = str(uuid.uuid4())  # unique identifier

# Побудова дерева
def build_sample_tree():
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)
    return root

# Генерація градієнта кольорів від темного до світлого
def generate_gradient_colors(n, base_color="#82EB45"):

    base_rgb = tuple(int(base_color[i:i+2], 16)/255. for i in (1, 3, 5))
    hsv = colorsys.rgb_to_hsv(*base_rgb)
    colors = []
    for i in range(n):
        v = 0.3 + 0.7 * (i / max(n - 1, 1))  # яскравість від 0.3 до 1.0
        rgb = colorsys.hsv_to_rgb(hsv[0], hsv[1], v)
        hex_color = '#' + ''.join(f'{int(c * 255):02X}' for c in rgb)
        colors.append(hex_color)
    return colors

# Обхід у глибину (DFS) зі стеком
def dfs_iterative(root):
    stack = [root]
    visited_order = []
    visited_ids = set()

    while stack:
        node = stack.pop()
        if node.id in visited_ids:
            continue
        visited_order.append(node)
        visited_ids.add(node.id)
        # правий додається першим, бо стек
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return visited_order

# Обхід у ширину (BFS) з чергою
def bfs_iterative(root):
    queue = deque([root])
    visited_order = []
    visited_ids = set()

    while queue:
        node = queue.popleft()
        if node.id in visited_ids:
            continue
        visited_order.append(node)
        visited_ids.add(node.id)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return visited_order

# Створення графа для NetworkX
def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

# Візуалізація дерева
def draw_tree(tree_root, title=""):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [tree.nodes[n]['color'] for n in tree.nodes()]
    labels = {n: tree.nodes[n]['label'] for n in tree.nodes()}

    plt.figure(figsize=(8, 5))
    plt.title(title)
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2000, node_color=colors, font_size=12)
    plt.show()

# Головна функція демонстрації
def visualize_traversal(traversal_func, title):
    root = build_sample_tree()
    visited_nodes = traversal_func(root)
    gradient = generate_gradient_colors(len(visited_nodes))

    for i, node in enumerate(visited_nodes):
        node.color = gradient[i]

    draw_tree(root, title=title)

# === Запуск ===

visualize_traversal(dfs_iterative, "DFS — Обхід у глибину")
visualize_traversal(bfs_iterative, "BFS — Обхід у ширину")
