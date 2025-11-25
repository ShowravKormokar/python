TreeT = {
    'A': [('B', 3), ('C', 5), ('D', 2)],
    'B': [('E', 4), ('F', 6)],
    'C': [('G', 1), ('H', 7)],
    'D': [('I', 3), ('J', 8)],
    'E': [('K', 2), ('L', 5)],
    'F': [('M', 1)],
    'G': [('N', 4)],
    'H': [('O', 3), ('P', 6)],
    'I': [('Q', 2)],
    'J': [('R', 3)],
    'K':[],'L':[],'M':[],'N':[],'O':[],'P':[],'Q':[],'R':[]
}

# Find Goal K, because last digit of my ID is 7 (ID: 222311077)

def dfs(node, target, visited=None, cost=0):
    if visited is None:
        visited = set()
    visited.add(node)
    print(node)
    if node == target:
        return cost
    for n, w in TreeT[node]:
        if n not in visited:
            c = dfs(n, target, visited, cost + w)
            if c is not None:
                return c
    return None

print("DFS Cost:", dfs('A', 'K'))