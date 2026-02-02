from collections import deque

goal = ((1,2,3),(4,5,6),(7,8,0))
moves = [(-1,0),(1,0),(0,-1),(0,1)]

def bfs(start):
    q = deque([(start, [])])
    visited = {start}

    while q:
        state, path = q.popleft()
        if state == goal:
            return path + [state]

        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    x, y = i, j

        for dx, dy in moves:
            nx, ny = x+dx, y+dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new = [list(r) for r in state]
                new[x][y], new[nx][ny] = new[nx][ny], new[x][y]
                new = tuple(tuple(r) for r in new)
                if new not in visited:
                    visited.add(new)
                    q.append((new, path + [state]))

    return None


start = ((1,2,3),(4,0,6),(7,5,8))
solution = bfs(start)

for s in solution:
    for r in s:
        print(r)
    print()