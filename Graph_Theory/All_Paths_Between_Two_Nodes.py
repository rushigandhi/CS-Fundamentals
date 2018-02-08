
def find_all_paths(graph, starting_node, ending_node, path = list()):

    path = path + [starting_node]

    if starting_node == ending_node:
        return [path]

    if starting_node not in graph:
        return []

    paths = list()

    for node in graph[starting_node]:

        if node not in path:
            new_paths = find_all_paths(graph, node, ending_node, path)

            for new_path in new_paths:

                paths.append(new_path)

    return paths


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

print("The path is", find_all_paths(graph, initial, final))