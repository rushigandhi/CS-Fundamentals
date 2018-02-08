def find_shortest_path(graph, starting_node, ending_node, path = list()):

    path = path + [starting_node]

    if starting_node == ending_node:
        return path

    if starting_node not in graph:
        return None

    shortest_path = None

    for node in graph[starting_node]:

        if node not in path:
            new_path = find_shortest_path(graph, node, ending_node, path)

            if new_path:
                if not shortest_path or len(new_path) < len(shortest_path):
                    shortest_path = new_path

    return shortest_path

graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}

print(graph)

print("Where are you?")
initial = input()

print("Where do you want to go?")
final = input()

print("The path is", find_shortest_path(graph, initial, final))