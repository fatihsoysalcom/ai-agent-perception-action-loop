import time

class AIAgent:
    def __init__(self, name, environment):
        self.name = name
        self.environment = environment
        self.internal_state = "initial"

    def perceive(self):
        # Simulate perception of the environment
        # In a real agent, this would involve sensors or data input
        perception_data = self.environment.get_state(self.name)
        print(f"[{self.name}] Perceived: {perception_data}")
        return perception_data

    def decide(self, perception_data):
        # Simulate decision-making based on perception and internal state
        # This is where the agent's 'intelligence' or logic resides
        if "danger" in perception_data and self.internal_state != "fleeing":
            action = "flee"
            self.internal_state = "fleeing"
        elif "food" in perception_data and self.internal_state != "eating":
            action = "eat"
            self.internal_state = "eating"
        else:
            action = "idle"
            self.internal_state = "observing"
        print(f"[{self.name}] Decided to: {action}")
        return action

    def act(self, action):
        # Simulate acting upon the environment
        # This would involve actuators or output signals
        print(f"[{self.name}] Acting: {action}")
        self.environment.perform_action(self.name, action)

    def run_cycle(self):
        # The core Perceive-Decide-Act loop
        perception = self.perceive()
        decision = self.decide(perception)
        self.act(decision)

class Environment:
    def __init__(self):
        self.state = {
            "agent1": "calm",
            "agent2": "calm"
        }
        self.events = []

    def get_state(self, agent_name):
        # In a real environment, this would be more complex
        # For this example, we simulate events affecting state
        current_agent_state = self.state.get(agent_name, "unknown")
        # Check for recent events that might affect perception
        recent_events_affecting_agent = [event for event in self.events if agent_name in event['targets']]
        if recent_events_affecting_agent:
            # Simple simulation: if any event targets the agent, it perceives it
            return f"{current_agent_state} with {', '.join([e['type'] for e in recent_events_affecting_agent])}"
        return current_agent_state

    def perform_action(self, agent_name, action):
        # Simulate the effect of an agent's action on the environment
        if action == "eat":
            print(f"[Environment] {agent_name} is eating. State becomes calm.")
            self.state[agent_name] = "calm"
            self.events.append({'type': 'food_consumed', 'targets': [agent_name]})
        elif action == "flee":
            print(f"[Environment] {agent_name} is fleeing. State becomes cautious.")
            self.state[agent_name] = "cautious"
            self.events.append({'type': 'danger_avoided', 'targets': [agent_name]})
        elif action == "idle":
            print(f"[Environment] {agent_name} is idle.")
            self.state[agent_name] = "observing"
        # Clear events that have been perceived and acted upon
        self.events = []

# --- Simulation Setup ---

# Create an environment
world = Environment()

# Create an AI agent
agent1 = AIAgent("AgentAlpha", world)

# Simulate some initial conditions or events
world.state["AgentAlpha"] = "calm"
world.events.append({'type': 'food_available', 'targets': ['AgentAlpha']})

print("--- Starting AI Agent Simulation ---")

# Run the agent's cycle for a few steps
for i in range(3):
    print(f"\n--- Cycle {i+1} ---")
    agent1.run_cycle()
    time.sleep(0.5) # Small delay for readability

# Simulate a change in environment to trigger a different decision
print("\n--- Simulating Danger ---")
world.state["AgentAlpha"] = "calm"
world.events.append({'type': 'danger_approaching', 'targets': ['AgentAlpha']})
agent1.run_cycle()

print("\n--- Simulation Ended ---")
