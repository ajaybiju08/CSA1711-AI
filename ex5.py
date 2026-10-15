from collections import deque

class State:
    def __init__(self, missionaries, cannibals, boat, parent=None):
        # State tracking numbers specifically on the LEFT bank
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat  # 1 for Left bank, 0 for Right bank
        self.parent = parent

    def is_valid(self):
        # Check boundary rules
        if not (0 <= self.missionaries <= 3 and 0 <= self.cannibals <= 3):
            return False
        
        # Calculate numbers on the RIGHT bank
        right_m = 3 - self.missionaries
        right_c = 3 - self.cannibals
        
        # Ensure missionaries are never outnumbered by cannibals on either side
        if self.missionaries > 0 and self.cannibals > self.missionaries:
            return False
        if right_m > 0 and right_c > right_m:
            return False
            
        return True

    def is_goal(self):
        # All missionaries and cannibals have crossed to the right bank (0 left)
        return self.missionaries == 0 and self.cannibals == 0 and self.boat == 0

    def __eq__(self, other):
        return (self.missionaries == other.missionaries and 
                self.cannibals == other.cannibals and 
                self.boat == other.boat)

    def __hash__(self):
        return hash((self.missionaries, self.cannibals, self.boat))

    def generate_successors(self):
        successors = []
        # Possible combinations of moves: (missionaries, cannibals) in the boat
        moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
        
        for m, c in moves:
            if self.boat == 1:  # Moving from Left to Right
                new_state = State(self.missionaries - m, self.cannibals - c, 0, self)
            else:               # Moving from Right to Left
                new_state = State(self.missionaries + m, self.cannibals + c, 1, self)
                
            if new_state.is_valid():
                successors.append(new_state)
        return successors

def solve_bfs():
    # Initial state: 3 Missionaries, 3 Cannibals, Boat on Left Bank
    start_state = State(3, 3, 1)
    if start_state.is_goal():
        return start_state

    queue = deque([start_state])
    visited = set([start_state])

    while queue:
        current_state = queue.popleft()

        if current_state.is_goal():
            return current_state

        for successor in current_state.generate_successors():
            if successor not in visited:
                visited.add(successor)
                queue.append(successor)
    return None

def print_solution(solution_state):
    path = []
    current = solution_state
    while current:
        path.append(current)
        current = current.parent
    path.reverse()

    print(f"{'Step':<5} | {'Left Bank (M, C)':<18} | {'Boat':<6} | {'Right Bank (M, C)':<18}")
    print("-" * 57)
    for i, state in enumerate(path):
        boat_side = "Left" if state.boat == 1 else "Right"
        left_side = f"({state.missionaries}, {state.cannibals})"
        right_side = f"({3 - state.missionaries}, {3 - state.cannibals})"
        print(f"{i:<5} | {left_side:<18} | {boat_side:<6} | {right_side:<18}")

if __name__ == "__main__":
    solution = solve_bfs()
    if solution:
        print("Solution found successfully!\n")
        print_solution(solution)
    else:
        print("No solution found.")
