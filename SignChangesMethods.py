"""
Description:
    - File to implement some methods to detect intervals containing a sign change
Author:
    - Sergio Quijano Rey
    - sergiquijano@gmail.com
"""

class SignChangesSolver:
    def __init__(self, function):
        self.function = function
        self.changes = []

    def reset_changes(self):
        self.changes = []

    def get_changes(self):
        return self.changes

class BruteForceMethod(SignChangesSolver):
    def __init__(self, function):
        # Super-Class initializer
        SignChangesSolver.__init__(self, function)
    
    def solve(self, lower, upper, iterations = 500):
        self.reset_changes()
        past_x = lower
        current_x = lower

        for i in range(iterations):
            # Next values are calculated
            past_x = current_x
            current_x = lower + ((upper - lower) / iterations) * i

            if self.function(past_x) * self.function(current_x) < 0:
                pair = (past_x, current_x)
                self.changes.append(pair)

        return self.changes
