# DFS 04
graphs = {
    '0': ['1'],
    '1': ['3'],
    '2': [],
    '3': ['2','4'],
    '4': ['5'],
    '5': ['7'],
    '6': [],
    '7': ['6']
}
def bfs(start):
    visited = []     
    queue = []       

    visited.append(start)
    queue.append(start)

    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        for neighbour in graphs[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
bfs('0')