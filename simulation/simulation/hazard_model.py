"""
BED v3 — Logistic Hazard Model (Public Version)

This file implements a simplified logistic hazard model used in the public
simulation engine. The private version includes additional calibration and
tuning logic that is intentionally excluded.
"""

import math

def logistic_hazard(recency, habit, responsiveness):
    """
    Public-safe logistic hazard function.
    """
    z = -0.5 + 0.1 * habit - 0.01 * recency + 0.5 * responsiveness
    return 1 / (1 + math.exp(-z))
