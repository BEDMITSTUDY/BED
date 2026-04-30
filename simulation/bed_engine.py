"""
BED v3 — Behavioral Engine (Public Version)

This file implements the public-facing behavioral state update logic for BED v3.
It includes recency, habit, and responsiveness updates, but excludes all private
tuning parameters and proprietary heuristics.
"""

class BehavioralState:
    def __init__(self, recency=0.0, habit=0.0, responsiveness=0.0):
        self.r = recency
        self.h = habit
        self.rho = responsiveness

    def update(self, action, event):
        """
        Public-safe update rules.
        These are simplified versions of the internal BED dynamics.
        """
        # Recency update
        self.r = 0 if event else self.r + 1

        # Habit update (bounded)
        self.h = max(0.0, min(1.0, self.h + 0.05 * (event - 0.5)))

        # Responsiveness update (bounded)
        if action == 1:
            self.rho = min(1.0, self.rho + 0.02)
        else:
            self.rho = max(0.0, self.rho - 0.01)

        return self
