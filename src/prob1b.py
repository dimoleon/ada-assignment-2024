import heapq

def dijkstra(graph, s, t):
    priority_queue = [(0, s)]  

    weights = {v: float('inf') for v in graph}
    weights[s] = 0

    while priority_queue:
        weight, v = heapq.heappop(priority_queue)

        if v == t:
            return weight

        for adj, length in graph[v]:
            weight_updated = max(weight, length)

            if weight_updated < weights[adj]:
                weights[adj] = weight_updated
                heapq.heappush(priority_queue, (weight_updated, adj))

    return float('inf') 
