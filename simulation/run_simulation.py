"""
BED v3 — Simulation Runner (Public Version)

Runs a synthetic simulation of behavioral state transitions, hazard events,
and CMDP policy decisions.
"""

import random
from bed_engine import BehavioralState
from hazard_model import HazardModel
from cmdp_solver import CMDPSolver

class SimulationRunner:
    def __init__(self, steps=100):
        self.steps = steps
        self.hazard = HazardModel()
        self.policy = CMDPSolver()

    def run(self):
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
