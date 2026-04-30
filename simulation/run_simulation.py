"""
class SimulationRunner:
    """
    Runs a public-safe BED v3 simulation over a fixed number of steps.
    """

    def __init__(self, steps=100):
        self.steps = steps
        self.hazard = HazardModel()
        self.policy = CMDPSolver()

    def run(self):
        """
        Execute the simulation loop.

        Returns:
            list[dict]: Time-series history of state, actions, and events.
        """

        random.seed(42)  # reproducibility
        state = BehavioralState()
        history = []

        for t in range(self.steps):
            action = self.policy.choose_action(state)
            p_event = self.hazard.hazard(state)
            event = 1 if random.random() < p_event else 0

            state.update(action, event)

            history.append({
                "t": t,
                "action": action,
                "event": event,
                "recency": state.r,
                "habit": state.h,
                "responsiveness": state.rho
            })

        return history
