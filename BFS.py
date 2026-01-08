graph = {
    '1':['2','7'],
    '2':['3','6'],
    '3':['4','5'],
     '4':[],
     '5':[],
     '6':[],
     '7':['8','9'],
     '8':['9'],
     '9':[],
     '10':[]
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