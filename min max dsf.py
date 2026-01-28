# Graph given
graph = {
    '1': ['2'],
    '2': ['5', '6'],
    '3': ['4'],
    '4': ['8'],
    '5': [],
    '6': [],
    '7': ['8'],
    '8': ['4']
}

# Utility values for terminal (leaf) nodes
values = {
    '5': 3,
    '6': 5,
    '4': 2,
    '8': 9
}

# Min-Max using DFS
def minimax(node, isMax):
    # Terminal node
    if node not in graph or len(graph[node]) == 0:
        return values.get(node, 0)

    if isMax:
        best = float('-inf')
        for child in graph[node]:
            best = max(best, minimax(child, False))
        return best
    else:
        best = float('inf')
        for child in graph[node]:
            best = min(best, minimax(child, True))
        return best


# Driver code
start_node = '1'
result = minimax(start_node, True)

print("Optimal Min-Max value is:", result)
 