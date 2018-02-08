def dfs_all_paths(graph, starting_node,  ending_node):

    stack = [(starting_node, [starting_node])]

    while stack:

        (vertex, path) = stack.pop()

        for next_node in graph[vertex] - set(path):

            if next_node == ending_node:
                yield path + [next_node]

            else:
                stack.append((next_node, path + [next_node]))


graph = {'A': set(['D', 'E']),
         'B': set(['F', 'G', 'E']),
         'C': set(['D', 'F']),
         'D': set(['F']),
         'E': set(['C', 'E']),
         'F': set(['A', 'B'])}

print(graph)

print("Where are you?")
initial = input()

print("Where do you want to go?")
final = input()

# all_paths = list()
#
# for i in dfs_all_paths(graph, initial, final):
#     all_paths.append(i)

print("The path is", list(dfs_all_paths(graph, initial, final)))