import numpy as np

def breakString(n, L):
    m = len(L)
    L = [-1] + L + [n-1]

    cost = np.full(shape=(m+2, m+2), fill_value=np.inf)

    for i in range(m+1):
        cost[i, i+1] = 0

    for delta in range(2, m + 2):
        for i in range(0, m + 2 - delta):
            j = i + delta

            minimum = np.inf
            for k in range(i+1, j):
                costValue = cost[i, k] + cost[k, j] + L[j] - L[i]
                if costValue < minimum:
                    minimum = costValue

            cost[i, j] = minimum

    return cost[0, m+1]
