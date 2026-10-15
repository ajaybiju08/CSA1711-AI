from collections import deque

def bfs(graph, start_node):
    """
    Performs a Breadth-First Search traversal on a graph starting from start_node.
    """
    # Keep track of visited nodes to avoid cycles
    visited = set()
    
    # Initialize a queue using deque for O(1) pops from the left side
    queue = deque([start_node])
    
    # Mark the starting node as visited
    visited.add(start_node)
    
    print("BFS Traversal Order: ", end="")
    
    # Loop continues until the queue is empty
    while queue:
        # Dequeue a vertex from the front of the queue
        current_node = queue.popleft()
        print(current_node, end=" ")
        
        # Get all adjacent neighbors of the dequeued node
        for neighbor in graph.get(current_node, []):
            # If a neighbor hasn't been visited yet, mark it visited and enqueue it
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    print()  # For a clean new line after traversal

# --- Driver Code ---
if __name__ == "__main__":
    # Define the graph using an adjacency list (Python Dictionary)
    # Visualizing a small graph: 
    #     A -> B, C
    #     B -> D, E
    #     C -> F
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    
    # Run BFS starting from node 'A'
    bfs(graph, 'A')
