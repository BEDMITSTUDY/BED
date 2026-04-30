"""
BED v3 — CMDP Solver (Public Version)

This file implements a simplified Constrained Markov Decision Process (CMDP)
policy used for the public simulation. The private version includes advanced
Lagrangian tuning and constraint shaping, which are intentionally excluded.
"""

class CMDPPolicy:
    def __init__(self, budget=0.1):
        self.budget = budget

    def choose_action(self, hazard):
        """
        Public-safe policy:
        - If hazard is high, send incentive with some probability.
        - If hazard is low, conserve budget.
        """
        if hazard > 0.25 and self.budget > 0:
            return 1
        return 0
