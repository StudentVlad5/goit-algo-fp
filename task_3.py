'''
Завдання 3. Дерева, алгоритм Дейкстри

Розробіть алгоритм Дейкстри для знаходження найкоротших шляхів у зваженому графі, використовуючи бінарну купу. Завдання включає створення графа, використання піраміди для оптимізації вибору вершин та обчислення найкоротших шляхів від початкової вершини до всіх інших.
'''


import heapq
import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(graph, start):
    # graph — словник суміжності: {вузол: [(сусід, вага), ...]}
    # start — початкова вершина

    # Ініціалізація відстаней до ∞, крім стартової вершини
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}

    # Бінарна купа: (відстань, вершина)
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Якщо ми знайшли кращу відстань раніше, ігноруємо цю
        if current_distance > distances[current_node]:
            continue

        # Перевірка сусідів
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # Якщо знайшли коротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))
                print("priority_queue", priority_queue)
    # Повертаємо словник з найкоротшими відстанями від стартової вершини
    return distances, previous_nodes

def build_path(prev_nodes, target):
    path = []
    while target:
        path.insert(0, target)
        target = prev_nodes[target]
    return path


def visualize_graph(graph_dict, shortest_path=None):
    G = nx.Graph()

    # Додаємо ребра
    for node, neighbors in graph_dict.items():
        for neighbor, weight in neighbors:
            G.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G)

    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1000, font_size=12)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    if shortest_path:
        # Підсвічування найкоротшого шляху
        path_edges = list(zip(shortest_path, shortest_path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=3)
        nx.draw_networkx_nodes(G, pos, nodelist=shortest_path, node_color='orange')

    plt.title("Граф і найкоротший шлях")
    plt.show()


# === Приклад ===
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}


'''
Граф повинен бути орієнтованим або неорієнтованим, але без від’ємних ваг.
heapq не дозволяє оновлювати ключ напряму — тому старі значення просто ігноруються при вилученні з купи.
'''


start = 'A'
target = 'D'
distances, prev_nodes = dijkstra(graph, start)
path = build_path(prev_nodes, target)

print(f"Найкоротша відстань від {start} до {target}: {distances[target]}")
print(f"Шлях: {' -> '.join(path)}")

visualize_graph(graph, shortest_path=path)
