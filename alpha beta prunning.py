import math

def alpha_beta(depth, nodeIndex, maximizingPlayer,
               values, alpha, beta):

    # Base case: leaf node reached
    if depth == 0:
        return values[nodeIndex]

    if maximizingPlayer:
        best = -math.inf

        for i in range(2):
            val = alpha_beta(depth - 1,
                             nodeIndex * 2 + i,
                             False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)

            # Beta cut-off
            if beta <= alpha:
                break

        return best

    else:
        best = math.inf

        for i in range(2):
            val = alpha_beta(depth - 1,
                             nodeIndex * 2 + i,
                             True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)

            # Alpha cut-off
            if beta <= alpha:
                break

        return best


# -------- MAIN PROGRAM --------
values = [3, 5, 6, 9, 1, 2, 0, -1]
depth = 3

result = alpha_beta(depth, 0, True,
                    values, -math.inf, math.inf)

print("Optimal value using Alpha-Beta Pruning:", result)