"""
BED v3 — Simulation Runner (Public Version)

This script runs a simple multi-step simulation using the public-safe BED
components. It is designed for reproducibility and demonstration purposes.
"""

from bed_engine import BehavioralState
from hazard_model import logistic_hazard
from cmdp_solver import CMDPPolicy

def run_simulation(steps=100):
    state = BehavioralState()
    policy = CMDPPolicy()

    logs = []

    for t in range(steps):
        hazard = logistic_hazard(state.r, state.h, state.rho)
        action = policy.choose_action(hazard)

        # Simulated event (Bernoulli)
        event = 1 if hazard > 0.3 else 0

        state.update(action, event)

        logs.append({
            "t": t,
            "recency": state.r,
            "habit": state.h,
            "responsiveness": state.rho,
            "hazard": hazard,
            "action": action,
            "event": event
        })

    return logs
