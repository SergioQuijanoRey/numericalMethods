"""
Description:
    - File to implement some function root solver methods
Author:
    - Sergio Quijano Rey
    - sergiquijano@gmail.com
"""

class BisectionMethod:
    def __init__(self):
        pass
    
    def solve(self, function, lower, upper, max_error, max_iterations):
        if function(lower) * function(upper) >= 0:
            print("Initial conditions of Bisection Method not met")
            print("f(lower) = {}".format(function(lower)))
            print("f(upper) = {}".format(function(upper)))

            # Error values
            return -1, -1

        # Initial values
        current_upper = upper
        current_lower = lower
        current_error = (current_upper - current_lower) / 2
        current_iteration = 0

        # Iterations of the method
        while current_error > max_error and current_iteration < max_iterations:
            current_middle = (current_upper + current_lower) / 2
            current_error = (current_upper - current_lower) / 2

            if function(current_middle) * function(current_lower) < 0:
                current_upper = current_middle
            elif function(current_middle) * function(current_upper) < 0:
                current_lower = current_middle
            elif function(current_middle) == 0:
                current_error = 0
            else:
                print("ERROR: unexpected situation at BisectionSolver.solve()")
                print("f({}) = {}".format(current_lower, function(current_lower)))
                print("f({}) = {}".format(current_upper, function(current_upper)))
                print("f({}) = {}".format(current_middle, function(current_middle)))

                # Error values
                current_middle = current_lower - 1
                current_error = -1

            current_iteration = current_iteration + 1
        
        return current_middle, current_error
