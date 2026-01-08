graph = {
    '1':['2'],
    '2':['5','6'],
    '3':['4'],
     '4':['8'],
     '5':[],
     '6':[],
     '7':['8'],
     '8':['4']
}
def bfs(start):
   visited = []
   queue = []
   visited.append(start)
   queue.append(start)
   while queue:
    node = queue.pop(0)
    print(node,end=" ")
    for neighbour in graph[node]:
       if neighbour not in visited:
         visited.append(neighbour) 
         queue.append(neighbour)
bfs('1')