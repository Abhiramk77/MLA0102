import heapq

def greedy_best_first_search(graph, heuristic, start, goal):
    visited = set()
    priority_queue = []

    # (heuristic value, node)
    heapq.heappush(priority_queue, (heuristic[start], start))

    while priority_queue:
        h, current = heapq.heappop(priority_queue)

        if current == goal:
            print("Goal reached:", current)
            return

        if current in visited:
            continue

        visited.add(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                heapq.heappush(priority_queue,
                               (heuristic[neighbor], neighbor))

    print("Goal not found")


# -------- MAIN --------
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

start_node = 'A'
goal_node = 'E'

greedy_best_first_search(graph, heuristic, start_node, goal_node)