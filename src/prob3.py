import numpy as np

def breakString(n, B):
    m = len(B)
    B = [-1] + B + [n-1]

    time_units = np.full(shape=(m+2, m+2), fill_value=np.inf)

    for i in range(m+1):
        time_units[i, i+1] = 0

    for delta in range(2, m + 2):
        for i in range(0, m + 2 - delta):
            j = i + delta

            minimum = np.inf
            for k in range(i+1, j):
                time_curr = time_units[i, k] + time_units[k, j] + B[j] - B[i]
                if time_curr < minimum:
                    minimum = time_curr

            time_units[i, j] = minimum

    return time_units[0, m+1]
