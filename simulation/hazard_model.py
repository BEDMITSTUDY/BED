class HazardModel:
    """
    Logistic hazard model for BED v3.

    Computes:
        P(event | state) = sigmoid( base + w_r*r + w_h*h + w_rho*rho )
    """

    def __init__(self, base_rate=0.05, recency_weight=-0.1,
                 habit_weight=0.4, responsiveness_weight=0.3):
        self.base = base_rate
        self.w_r = recency_weight
        self.w_h = habit_weight
        self.w_rho = responsiveness_weight

    def hazard(self, state) -> float:
        """Compute event probability given behavioral state."""
        z = (
            self.base +
            self.w_r * state.r +
            self.w_h * state.h +
            self.w_rho * state.rho
        )
        return 1 / (1 + math.exp(-z))

