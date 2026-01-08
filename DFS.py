graph = {
    '1': ['2', '3'],
    '2': ['4', '5'],
    '3': ['6'],
    '4': [],
    '5': [],
    '6': []
}

def dfs(start):
    visited = []
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")
            visited.append(node)
            # reverse to maintain left-to-right order
            stack.extend(reversed(graph[node]))

dfs('1')
