import itertools

def calculate_total_distance(route, graph):
    """
    Calculates the total distance of a specific route, 
    including the return journey to the starting city.
    """
    total_dist = 0
    num_cities = len(route)
    
    for i in range(num_cities):
        current_city = route[i]
        # Get the next city in the list, wrapping back to the first city at the end
        next_city = route[(i + 1) % num_cities] 
        total_dist += graph[current_city][next_city]
        
    return total_dist

def solve_tsp_brute_force(graph):
    """
    Finds the optimal TSP route and the minimum distance 
    by checking all possible city permutations.
    """
    num_cities = len(graph)
    cities = list(range(num_cities))
    
    # We fix the starting city to avoid checking redundant cyclic permutations
    start_city = cities[0]
    other_cities = cities[1:]
    
    min_distance = float('inf')
    optimal_route = None
    
    # Generate all permutations of the remaining cities
    for perm in itertools.permutations(other_cities):
        # Create a full tour: Start -> [Permutation] -> Start
        current_route = [start_city] + list(perm)
        current_distance = calculate_total_distance(current_route, graph)
        
        # Update if a shorter path is found
        if current_distance < min_distance:
            min_distance = current_distance
            optimal_route = current_route
            
    return optimal_route, min_distance

# --- Example Usage ---
if __name__ == "__main__":
    # Distance matrix (Adjacency Matrix) representing distances between 4 cities (0, 1, 2, 3)
    # graph[i][j] represents the distance from city i to city j
    distance_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    
    best_route, min_cost = solve_tsp_brute_force(distance_matrix)
    
    # Format output for printing (showing the complete loop back to start)
    complete_loop = best_route + [best_route[0]]
    
    print("--- Traveling Salesman Problem Optimal Solution ---")
    print(f"Optimal Route Matrix Order: {' -> '.join(map(str, complete_loop))}")
    print(f"Minimum Distance / Cost   : {min_cost}")
