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

# Super-Class
#===============================================================================
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
        """Aproximates the root of a function. This general implementation can
           be changed in child classes. However, the best way of changing the 
           behaviour is changing the function self.choose_next_middle()

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

        if self.interval_check(lower, upper) == False:
            print("Initial conditions of Bisection Method not met")
            print("f(lower) = {}".format(self.function(lower)))
            print("f(upper) = {}".format(self.function(upper)))

            # Error values
            return -1, -1

        # Initial values
        current_upper = upper
        current_lower = lower
        current_iteration = 0

        current_middle = upper
        past_middle = lower
        iteration_error = max_error

        # Iterations of the method
        while iteration_error >= max_error and current_iteration < max_iterations:
            past_middle = current_middle
            current_middle = self.choose_next_middle(current_lower, current_upper)

            # Bounds are move
            current_lower, current_upper = self.move_bound_to_middle(current_lower, current_middle, current_upper)

            # Integrity check
            if current_lower < lower or current_upper > upper:
                print("ERROR! Bad bound on BisectionMethod.solve()")
                return lower - 1, upper + 1

            # Verbose output
            if verbose == True:
                print("Interation {it}:\t{val}".format(it = current_iteration, val = current_middle))

            self.iteration_values.append(current_middle)

            iteration_distance = abs(current_middle - past_middle)
            current_iteration = current_iteration + 1
        
        return current_middle, iteration_error
    
    def move_bound_to_middle(self, lower, middle, upper):
        """Moves either the lower bound or upper bound to the middle.
            
            Parameters:
                - lower: the lower bound, it can be MODIFIED
                - middle: the middle bound
                - upper: the upper bound, it can be MODIFIED
            Returns:
                - The pair new_lower, new_upper
        """
        if self.function(middle) * self.function(lower) < 0:
            return lower, middle
        elif self.function(middle) * self.function(upper) < 0:
            return middle, upper
        elif self.function(middle) == 0:
            return middle, middle
        else:
            print("ERROR: unexpected situation at BisectionSolver.solve()")
            print("f({}) = {}".format(lower, self.function(lower)))
            print("f({}) = {}".format(upper, self.function(upper)))
            print("f({}) = {}".format(middle, self.function(middle)))

            # Error Code
            return lower - 1, upper + 1

    def interval_check(self, lower, upper):
        """Checks if the interval guarantees a root

           Usually this means that the function evaluated on the sign of lower bound 
           is different from the sign of the upper bound. However, this check
           can be modified in child classes
        """
        return self.function(lower) * self.function(upper) < 0
    
    def choose_next_middle(self, lower, upper):
        """Chooses the next middle point. 

        This function usually determinates the method which is beign used

        Parameters:
            - lower: the lower bound of the interval
            - upper: the upper bound of the interval
        Returns:
            - The middle point chosen
        """
        pass

# Super-Class
#===============================================================================
class IterationRootSolver(RootSolver):
    def __init__(self, function):
        print("DEBUG 01")
        RootSolver.__init__(function)
        print("DEBUG 02")

    def solve(self, seed, max_error = 0, max_iterations=MAX_ITERATIONS, verbose = False):
        """Aproximates the root of a function. This general implementation can
           be changed in child classes. However, the best way of changing the 
           behaviour is changing the function self.choose_next_middle()

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

        # Initial values
        value = seed
        iteration = 0
        iteration_error = max_error

        # Iterations of the method
        while iteration_error >= max_error and iteration < max_iterations:
            past_value = value

            # Next iteration is calculated
            value = self.calculate_next_value(value)

            # Verbose output
            if verbose == True:
                print("Interation {it}:\t{val}".format(it = iteration, val = value))

            self.iteration_values.append(value)

            iteration_error = abs(value - past_value)
            iteration = iteration + 1
        
        return value, iteration_error
    
    def calculate_next_value(self, value):
        pass

# BisectionMethod
#===============================================================================
class BisectionMethod(RootSolver):
    def __init__(self, function):
        """Initializer of the class"""
        # Init de la clase base
        RootSolver.__init__(self, function)

    def choose_next_middle(self, lower, upper):
        return (upper + lower) / 2
    

# RegulaFalsiMethod
#===============================================================================
class RegulaFalsiMethod(RootSolver):
    """Regula-Falsi Method
    
        Consists on a mixed method of bisection and secant methods
        Use as next middle point the intersection with x axis of the line  f(b) to f(a)
    """

    def __init__(self, function):
        """Initializer of the class"""
        # Base constructor
        RootSolver.__init__(self, function)
    
    def choose_next_middle(self, upper, lower):
        """Private function to calculate the intersection with x axis of the line  f(upper) to f(lower)"""
        return (self.function(upper) * lower - self.function(lower) * upper) / (self.function(upper) - self.function(lower))

# Newton-Raphson
#===============================================================================
class NewtonRaphsonMethod(IterationRootSolver):
    def __init__(self, function, derivative):
        self.function = function
        self.derivative = derivative

    def calculate_next_value(self, value):
        return value - (self.function(value)) / (self.derivative(value))
