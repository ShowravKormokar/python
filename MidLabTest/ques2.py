def dfs(node, target, visited=None, cost=0):
    if visited is None:
        visited = set()
    if node == target:
        return cost
    visited.add(node)
    print(node)
    for n, w in graph[node]:
        if n not in visited:
            c = dfs(n, target, visited, cost + w)
            if c is not None:
                return c
    return None

print("DFS Cost:", dfs('A', 'H'))