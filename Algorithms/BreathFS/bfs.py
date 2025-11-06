# Breath First Search (BFS) Algorithm Implementation
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

def bfs(start,goal):
    queue = [(start, 0)]  # Queue of tuples (node, cumulative_cost)
    visited = set()  # Set to keep track of visited nodes
    while queue:
        node, cost = queue.pop(0)  # Dequeue the first element
        print(f"Visiting Node: {node} with Cumulative Cost: {cost}")
        if node == goal:
            return cost  # Return the cumulative cost if goal is found
        if node not in visited:
            visited.add(node)  # Mark the node as visited
            for neighbor, edge_cost in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, cost + edge_cost))  # Enqueue neighbor with updated cost

print("BFS Cost: ", bfs('A', 'H'))

# minimum cost path from A to H is 5 (A -> C -> H). min(cost)
# Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges.
# Space Complexity: O(V) for the queue and visited set.