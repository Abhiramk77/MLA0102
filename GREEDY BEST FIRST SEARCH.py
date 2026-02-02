import heapq

def greedy_best_first_search(graph, heuristic, start, goal):
    visited = set()
    pq = []

    heapq.heappush(pq, (heuristic[start], start))

    while pq:
        _, current = heapq.heappop(pq)

        if current == goal:
            print("Goal reached:", current)
            return

        if current in visited:
            continue

        visited.add(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                heapq.heappush(pq, (heuristic[neighbor], neighbor))

    print("Goal not found")


# Main
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'E': 0,
    'F': 3,
    'G': 4
}

greedy_best_first_search(graph, heuristic, 'A', 'E')