from collections import deque

def water_jug(cap1, cap2, goal):
    visited = set()
    q = deque()

    q.append((0, 0))
    visited.add((0, 0))

    while q:
        x, y = q.popleft()

        if x == goal or y == goal:
            print("Goal reached:", (x, y))
            return

        next_states = [
            (cap1, y),   # Fill jug1
            (x, cap2),   # Fill jug2
            (0, y),      # Empty jug1
            (x, 0),      # Empty jug2
            (x - min(x, cap2 - y), y + min(x, cap2 - y)),  # jug1 -> jug2
            (x + min(y, cap1 - x), y - min(y, cap1 - x))   # jug2 -> jug1
        ]

        for state in next_states:
            if state not in visited:
                visited.add(state)
                q.append(state)

    print("No solution")


# Main
water_jug(4, 3, 2)