"""
BED v3 — CMDP Solver (Public Version)

This module implements a simplified Constrained Markov Decision Process solver.
It selects actions (incentives) subject to a budget constraint.
"""

class CMDPSolver:
    def __init__(self, budget=100, cost_per_action=1):
        self.budget = budget
        self.cost = cost_per_action

    def choose_action(self, state):
        """
        Public-safe policy:
        - If responsiveness is low, offer an incentive (action=1)
        - If budget is exhausted, no incentive (action=0)
        """
        if self.budget < self.cost:
            return 0

        if state.rho < 0.5:
            self.budget -= self.cost
            return 1

        return 0
