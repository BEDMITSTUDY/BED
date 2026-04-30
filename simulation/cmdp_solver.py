class CMDPSolver:
    """
    Simplified public-safe CMDP policy for BED v3.

    Attributes:
        budget (int): Remaining incentive budget.
        cost (int): Cost per incentive action.
    """

    def __init__(self, budget=100, cost_per_action=1):
        self.budget = budget
        self.cost = cost_per_action

    def choose_action(self, state) -> int:
        """
        Select an action subject to budget constraints.

        Policy:
            - If budget is exhausted → no incentive.
            - If responsiveness is below threshold → give incentive.
            - Otherwise → no incentive.

        Args:
            state (BehavioralState): Current behavioral state.

        Returns:
            int: 1 for incentive, 0 otherwise.
        """

        if self.budget < self.cost:
            return 0

        if state.rho < 0.5:
            self.budget -= self.cost
            return 1

        return 0
