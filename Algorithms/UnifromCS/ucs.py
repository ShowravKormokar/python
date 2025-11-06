# Uniform Cost Search (UCS) implementation in Python

# Uniform Cost Search (UCS) implementation in Python

# Adjacency List representation
graph = {
    'A': [('B', 2), ('C', 3), ('D', 5)],
    'B': [('E', 4), ('F', 1)],
    'C': [('G', 6), ('H', 2)],
    'D': [('I', 3), ('J', 4)],
    'E': [],
    'F': [],
    'G': [],
    'H': [],
    'I': [],
    'J': []
}

def ucs(start, goal):
    # queue holds tuples of (cost, node)
    queue = [(0, start)]
    visited = set()

    while queue:
        # Sort by cost (lowest first)
        queue.sort(key=lambda x: x[0])
        cost, node = queue.pop(0)

        print(f"Visiting Node: {node} with Cumulative Cost: {cost}")

        if node == goal:
            return cost  # Found goal

        if node not in visited:
            visited.add(node)
            for neighbor, edge_cost in graph[node]:
                total_cost = cost + edge_cost
                queue.append((total_cost, neighbor))

    return float('inf')  # If goal not reachable

# Run UCS
print("UCS Cost:", ucs('A', 'H'))

# minimum cost path from A to H is 5 (A -> C -> H). min(cost)
# Time Complexity: O((V + E) log V) where V is the number of vertices and E is the number of edges.
# Space Complexity: O(V) for the priority queue and visited set.