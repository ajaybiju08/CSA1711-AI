import heapq

class Node:
    """Represents a coordinate in the grid."""
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        
        self.g = 0  # Cost from start to current node
        self.h = 0  # Estimated cost from current node to end (heuristic)
        self.f = 0  # Total cost (f = g + h)

    # Define less-than for the priority queue to compare f-values
    def __lt__(self, other):
        return self.f < other.f

    # Helper to check if two nodes have the same coordinates
    def __eq__(self, other):
        return self.position == other.position


def heuristic(current, target):
    """
    Calculates Manhattan distance between two points.
    Suitable for a grid where movements are restricted to up, down, left, right.
    """
    return abs(current[0] - target[0]) + abs(current[1] - target[ target[1] ])


def a_star_search(grid, start, end):
    """
    Implements the A* algorithm on a 2D grid.
    0 represents open path, 1 represents an obstacle.
    """
    # Create start and end nodes
    start_node = Node(start)
    end_node = Node(end)

    # Initialize open (priority queue) and closed sets
    open_list = []
    closed_set = set()

    # Heapify the open list and add the starting node
    heapq.heappush(open_list, start_node)

    # Keep track of node locations in the open list to optimize g-score updates
    open_dict = {start: start_node}

    rows, cols = len(grid), len(grid[0])

    while open_list:
        # Get the node with the lowest f value
        current_node = heapq.heappop(open_list)
        current_pos = current_node.position
        
        # Remove from our tracking dictionary
        if current_pos in open_dict:
            del open_dict[current_pos]

        # Add current node position to closed set
        closed_set.add(current_pos)

        # Goal reached: reconstruct and return path
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]  # Return reversed path

        # Generate neighbors (Up, Down, Left, Right)
        neighbors = [
            (current_pos[0] - 1, current_pos[1]), # Up
            (current_pos[0] + 1, current_pos[1]), # Down
            (current_pos[0], current_pos[1] - 1), # Left
            (current_pos[0], current_pos[1] + 1)  # Right
        ]

        for next_pos in neighbors:
            # 1. Ensure neighbor is within grid boundaries
            if not (0 <= next_pos[0] < rows and 0 <= next_pos[1] < cols):
                continue

            # 2. Ensure neighbor is walkable (not an obstacle)
            if grid[next_pos[0]][next_pos[1]] == 1:
                continue

            # 3. Skip if neighbor is already evaluated
            if next_pos in closed_set:
                continue

            # Calculate tentative g-score
            tentative_g = current_node.g + 1

            # 4. Process the neighbor
            if next_pos in open_dict:
                # If neighbor is in open list but the new path is worse, skip it
                if tentative_g >= open_dict[next_pos].g:
                    continue
                # Otherwise, we found a better path, so we will update it below
                neighbor_node = open_dict[next_pos]
            else:
                # Create a completely new node
                neighbor_node = Node(next_pos, current_node)
                open_dict[next_pos] = neighbor_node

            # Update scores and parent
            neighbor_node.parent = current_node
            neighbor_node.g = tentative_g
            neighbor_node.h = heuristic(next_pos, end_node.position)
            neighbor_node.f = neighbor_node.g + neighbor_node.h

            # If it was a new node, push it to the priority queue
            if neighbor_node not in open_list:
                heapq.heappush(open_list, neighbor_node)

    return None  # Return None if no path exists


# --- Example Usage ---
if __name__ == "__main__":
    # Define a 5x5 grid. 0 = Walkable, 1 = Wall/Obstacle.
    example_grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0]
    ]

    start_point = (0, 0)
    end_point = (4, 4)

    shortest_path = a_star_search(example_grid, start_point, end_point)

    if shortest_path:
        print(f"Path found: {shortest_path}")
    else:
        print("No path found.")
