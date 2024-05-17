def dfs(graph, s, t, L, visited = set()):
    if s == t:
        return True
    visited.add(s)
    
    for adj, length in graph[s]:
        if length <= L and adj not in visited:
            if dfs(graph, adj, t, L, visited):
                return True
    
    return False