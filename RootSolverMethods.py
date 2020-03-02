"""
Description:
    - File to implement some function root solver methods
Author:
    - Sergio Quijano Rey
    - sergiquijano@gmail.com
"""

# Global parameters
#===============================================================================
MAX_ITERATIONS = 500

class BisectionMethod:
    def __init__(self, function):
        self.function = function
        self.values = []
    
    def solve(self, lower, upper, max_error = 0, max_iterations=MAX_ITERATIONS, verbose = False):
        # New values are set
        self.values = []

        if self.function(lower) * self.function(upper) >= 0:
            print("Initial conditions of Bisection Method not met")
            print("f(lower) = {}".format(self.function(lower)))
            print("f(upper) = {}".format(self.function(upper)))

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

            if self.function(current_middle) * self.function(current_lower) < 0:
                current_upper = current_middle
            elif self.function(current_middle) * self.function(current_upper) < 0:
                current_lower = current_middle
            elif self.function(current_middle) == 0:
                current_error = 0
            else:
                print("ERROR: unexpected situation at BisectionSolver.solve()")
                print("f({}) = {}".format(current_lower, self.function(current_lower)))
                print("f({}) = {}".format(current_upper, self.function(current_upper)))
                print("f({}) = {}".format(current_middle, self.function(current_middle)))

                # Error values
                current_middle = current_lower - 1
                current_error = -1

            if verbose == True:
                print("Interation {it}:\t{val}".format(it = current_iteration, val = current_middle))

            self.values.append(current_middle)

            current_iteration = current_iteration + 1
        
        return current_middle, current_error
    
    def get_values(self):
        return self.values

class RegulaFalsiMethod:
    def __init__(self):
        pass
    
    def solve(self, function, lower, upper, max_error, max_iterations):
        # Initial parameters
        current_iteration = 0
        current_lower = lower
        current_upper = upper
        current_middle = current_lower
        iteration_error = max_error

        # Repetetive calculations
        b = function(0)

        while current_iteration < max_iterations and iteration_error > max_error:
            # Next cut with the x-axis between f(b) and f(a)
            past_middle = current_middle
            current_middle = (-b) / ((function(current_upper) - function(current_lower)) / (current_upper - current_lower))

            # We choose which limit to move
            if function(current_middle) * function(current_lower) < 0:
                current_upper = current_middle
            elif function(current_middle) * function(current_upper) < 0:
                current_lower = current_middle
            elif function(current_middle) == 0:
                current_error = 0
            else:
                print("ERROR: unexpected situation at RegulaFalsiMethod.solve()")
                print("f({}) = {}".format(current_lower, function(current_lower)))
                print("f({}) = {}".format(current_upper, function(current_upper)))
                print("f({}) = {}".format(current_middle, function(current_middle)))

            current_iteration = current_iteration + 1
            iteration_error = abs(current_middle - past_middle)

        return current_middle, iteration_error

class SecantMethod:
    def __init__(self):
        pass
    
    def solve(self, function, lower, upper, max_error, max_iterations):
        # Initial values
        current_iteration = 0
        current_x = upper
        past_x = lower
        iteration_error = current_x - past_x

        # Aproximation of the derivative
        def derivative_aprox(current_val, past_val):
            return (function(current_val) - function(past_val)) / (current_val - past_val)

        # Calculations are done
        while current_iteration < max_iterations and iteration_error > max_error:
            current_x, past_x = current_x - (function(current_x)) / (derivative_aprox(current_x, past_x)), current_x
            iteration_error = current_x - past_x

        # Results are returned
        return current_x, iteration_error
