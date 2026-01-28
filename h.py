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
visited = set()

def DFS(node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbour in graphs[node]:
            DFS(neighbour)
DFS('0')