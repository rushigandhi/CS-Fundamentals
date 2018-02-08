def find_path(graph, starting_node, ending_node, path = list()):

    path = path + [starting_node]

    if starting_node == ending_node:
        return path

    if starting_node not in graph:
        return None

    for node in graph[starting_node]:

        if node not in path:
            new_path = find_path(graph, node, ending_node, path)

            if new_path:
                return new_path

    return None

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

print("The path is", find_path(graph, initial, final))