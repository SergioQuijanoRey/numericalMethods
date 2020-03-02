"""
Description:
    - File to implement some fucntion root solver methods
Author:
    - Sergio Quijano Rey
    - sergiquijano@gmail.com
"""

# Global parameters
#===============================================================================
MAX_ITERATIONS = 500

class RootSolver:
    """Base class of the root solvers. Need to be implemented by child classes"""
    def __init__(self, function):
        """Initializer of the class"""
        self.function = function
        self.iteration_values = []

    def get_iteration_values(self):
        """Getter of the iteration values"""
        return self.iteration_values
    
    def reset_iteration_values(self):
        """Resets the iteration value stored during a process"""
        self.iteration_values = []
    
    def solve(self, lower, upper, max_error = 0, max_iterations=MAX_ITERATIONS, verbose = False):
        """Aproximates the root of a function. It needs to be implemented in child classes

        Parameters:
            - lower: the lower bound of the interval
            - upper: the upper bound of the interval
            - max_error: the max error permited. The error has to be interpreted 
                         by the child classes (iteration error, real error...)
            - max_iterations: the maximun iterations allowed, even if error is above max error
            - verbose: either show the process or not
        """
        pass

class BisectionMethod(RootSolver):
    def __init__(self, function):
        """Initializer of the class"""
        # Init de la clase base
        RootSolver.__init__(self, function)
    
    def solve(self, lower, upper, max_error = 0, max_iterations=MAX_ITERATIONS, verbose = False):
        """Aproximates the root of a function

        Parameters:
            - lower: the lower bound of the interval
            - upper: the upper bound of the interval
            - max_error: the max error permited. The error has to be interpreted 
                         by the child classes (iteration error, real error...)
            - max_iterations: the maximun iterations allowed, even if error is above max error
            - verbose: either show the process or not
        """
        # New values are set
        self.reset_iteration_values()

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

            self.iteration_values.append(current_middle)

            current_iteration = current_iteration + 1
        
        return current_middle, current_error

class RegulaFalsiMethod(RootSolver):
    """Regula-Falsi Method
    
        Consists on a mixed method of bisection and secant methods
        Use as next middle point the intersection with x axis of the line  f(b) to f(a)
    """

    def __init__(self, function):
        """Initializer of the class"""
        # Base constructor
        RootSolver.__init__(self, function)
    
    def solve(self, lower, upper, max_error = 0, max_iterations=MAX_ITERATIONS, verbose = False):
        """Aproximates the root of a function

        Parameters:
            - lower: the lower bound of the interval
            - upper: the upper bound of the interval
            - max_error: the max error permited. The error has to be interpreted 
                         by the child classes (iteration error, real error...)
            - max_iterations: the maximun iterations allowed, even if error is above max error
            - verbose: either show the process or not
        """

        # Initial values
        current_lower = lower
        current_upper = upper
        current_middle = lower
        iteration_distance = max_error
        iteration = 0

        # Fresh list of iteration aproximations
        self.reset_iteration_values()

        # Aproximation Loop
        while iteration < max_iterations and iteration_distance >= max_error:
            past_middle = current_middle
            current_middle = self.__calculate_middle(current_upper, current_lower)
            iteration_distance = current_middle - past_middle

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
                print("Iteration {it}:\t{val}".format(it = iteration, val = current_middle))

            self.iteration_values.append(current_middle)
            iteration = iteration + 1

        return current_middle, iteration_distance
    
    def __calculate_middle(self, upper, lower):
        """Private function to calculate the intersection with x axis of the line  f(upper) to f(lower)"""
        return (self.function(upper) * lower - self.function(lower) * upper) / (self.function(upper) - self.function(lower))
