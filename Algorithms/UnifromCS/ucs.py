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
    import heapq

    # Priority queue to store (cumulative_cost, node)
    priority_queue = [(0, start)]
    visited = set()  # Set to keep track of visited nodes

    while priority_queue:
        cost, node = heapq.heappop(priority_queue)  # Dequeue the element with the lowest cost
        print(f"Visiting Node: {node} with Cumulative Cost: {cost}")
        
        if node == goal:
            return cost  # Return the cumulative cost if goal is found
        
        if node not in visited:
            visited.add(node)  # Mark the node as visited
            
            for neighbor, edge_cost in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (cost + edge_cost, neighbor))  # Enqueue neighbor with updated cost  

print("UCS Cost: ", ucs('A', 'H'))

# minimum cost path from A to H is 5 (A -> C -> H). min(cost)
# Time Complexity: O((V + E) log V) where V is the number of vertices and E is the number of edges.
# Space Complexity: O(V) for the priority queue and visited set.