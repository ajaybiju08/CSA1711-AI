from typing import Dict, List, Optional, Generic, TypeVar

# Define generic types for flexibility
V = TypeVar('V')  # Variable type
D = TypeVar('D')  # Domain type


class CSP(Generic[V, D]):
    """Class representing a generic Constraint Satisfaction Problem."""
    
    def __init__(self, variables: List[V], domains: Dict[V, List[D]]):
        self.variables: List[V] = variables  # Variables to be assigned
        self.domains: Dict[V, List[D]] = domains  # Possible values for each variable
        self.constraints: Dict[V, List[V]] = {v: [] for v in variables}
        
    def add_constraint(self, v1: V, v2: V):
        """Adds a binary constraint between two adjacent variables."""
        if v2 not in self.constraints[v1]:
            self.constraints[v1].append(v2)
        if v1 not in self.constraints[v2]:
            self.constraints[v2].append(v1)

    def is_consistent(self, variable: V, assignment: Dict[V, D], value: D) -> bool:
        """Checks if the assigned value satisfies constraints with neighbors."""
        for neighbor in self.constraints[variable]:
            if neighbor in assignment and assignment[neighbor] == value:
                return False
        return True

    def backtracking_search(self, assignment: Dict[V, D] = {}) -> Optional[Dict[V, D]]:
        """Classic depth-first backtracking search to find a solution."""
        # Base case: assignment is complete
        if len(assignment) == len(self.variables):
            return assignment

        # Select an unassigned variable
        unassigned: List[V] = [v for v in self.variables if v not in assignment]
        first = unassigned[0]

        # Try assigning each value in the variable's domain
        for value in self.domains[first]:
            if self.is_consistent(first, assignment, value):
                assignment[first] = value
                
                # Recursively attempt to find a solution down this branch
                result = self.backtracking_search(assignment)
                if result is not None:
                    return result
                
                # Undo the assignment (backtrack) if it failed down the line
                del assignment[first]
                
        return None


# --- Map Coloring Problem Setup ---
if __name__ == "__main__":
    # 1. Define the regions (Variables) of Australia as an example
    regions = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]
    
    # 2. Define the available colors (Domains) for each region
    colors = ["Red", "Green", "Blue"]
    domains = {region: colors.copy() for region in regions}
    
    # 3. Instantiate the CSP framework
    map_csp = CSP(regions, domains)
    
    # 4. Define the adjacency borders (Constraints)
    # No two bordering regions can share the same color
    borders = [
        ("WA", "NT"), ("WA", "SA"),
        ("NT", "SA"), ("NT", "Q"),
        ("SA", "Q"),  ("SA", "NSW"), ("SA", "V"),
        ("Q", "NSW"),
        ("NSW", "V"),
        # Tasmania ("T") is an island and has no borders here
    ]
    
    for v1, v2 in borders:
        map_csp.add_constraint(v1, v2)
        
    # 5. Run the solver
    solution = map_csp.backtracking_search()
    
    # 6. Display Output
    if solution is None:
        print("No valid coloring solution found.")
    else:
        print("Success! Valid Map Coloring Found:")
        print("-" * 35)
        for region, color in sorted(solution.items()):
            print(f"Region: {region:4} -> Color: {color}")
