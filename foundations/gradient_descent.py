class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        minimiser=init
        for i in range(iterations):
            der=2*minimiser
            minimiser=minimiser-learning_rate*der

        return round(minimiser,5)

