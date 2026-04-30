class BehavioralState:
    """
    Public-facing behavioral state for BED v3.

    Attributes:
        r (float): Recency state.
        h (float): Habit strength.
        rho (float): Incentive responsiveness.
    """

    def __init__(self, recency=0.0, habit=0.0, responsiveness=0.0):
        self.r = recency
        self.h = habit
        self.rho = responsiveness

    def update(self, action: int, event: int):
        """
        Update the behavioral state using simplified public-safe dynamics.

        Args:
            action (int): 1 if an incentive is given, 0 otherwise.
            event (int): 1 if an event occurred, 0 otherwise.

        Returns:
            BehavioralState: Updated state.
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
