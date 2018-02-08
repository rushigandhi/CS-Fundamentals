def bfs_all_paths(graph, starting_node,  ending_node):

    queue = [(starting_node, [starting_node])]

    while queue:

        (vertex, path) = queue.pop()

        for next_node in graph[vertex] - set(path):

            if next_node == ending_node:
                yield path + [next_node]

            else:
                queue.append((next_node, path + [next_node]))


graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

print(graph)

print("Where are you?")
initial = input()

print("Where do you want to go?")
final = input()

# all_paths = list()
#
# for i in dfs_all_paths(graph, initial, final):
#     all_paths.append(i)

print("The path is", list(bfs_all_paths(graph, initial, final)))