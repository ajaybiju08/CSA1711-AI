import random
import time

class VacuumEnvironment:
    def __init__(self):
        # 0 = Clean, 1 = Dirty
        self.location_status = {
            'A': random.choice([0, 1]),
            'B': random.choice([0, 1])
        }
        # Randomly place the vacuum cleaner in room A or B
        self.vacuum_location = random.choice(['A', 'B'])

    def display_status(self):
        print(f"Current State -> Room A: {'DIRTY' if self.location_status['A'] else 'CLEAN'} | "
              f"Room B: {'DIRTY' if self.location_status['B'] else 'CLEAN'}")
        print(f"Vacuum is currently in Room: {self.vacuum_location}\n")

    def is_completely_clean(self):
        return self.location_status['A'] == 0 and self.location_status['B'] == 0


class ReflexVacuumAgent:
    def __init__(self):
        self.cost = 0  # Track total performance cost/moves

    def act(self, environment):
        current_loc = environment.vacuum_location
        current_status = environment.location_status[current_loc]

        print(f"[Percept] Location: {current_loc}, Status: {'DIRTY' if current_status == 1 else 'CLEAN'}")

        # Rule 1: If the current room is dirty, suck the dirt
        if current_status == 1:
            print("Action: SUCK")
            environment.location_status[current_loc] = 0
            self.cost += 1
            print(f"-> Room {current_loc} has been cleaned.")
        
        # Rule 2: If clean and in Room A, move right to Room B
        elif current_loc == 'A':
            print("Action: MOVE RIGHT")
            environment.vacuum_location = 'B'
            self.cost += 1
            
        # Rule 3: If clean and in Room B, move left to Room A
        elif current_loc == 'B':
            print("Action: MOVE LEFT")
            environment.vacuum_location = 'A'
            self.cost += 1


# --- Main Simulation Execution ---
if __name__ == "__main__":
    print("=== Initializing Vacuum Cleaner Simulation ===")
    env = VacuumEnvironment()
    agent = ReflexVacuumAgent()
    
    env.display_status()
    time.sleep(1)

    step = 1
    while not env.is_completely_clean():
        print(f"--- Step {step} ---")
        agent.act(env)
        env.display_status()
        step += 1
        time.sleep(1)

    print("========================================")
    print("Goal State Reached: All rooms are CLEAN!")
    print(f"Total path cost (actions taken): {agent.cost}")
    print("========================================")
