"""
Description:
    - File to describe the class RootSolver
Author:
    - Sergio Quijano Rey
    - sergiquijano@gmail.com
"""

class RootSolver:
    def __init__(self, method):
        self.method = method
        
    def solve(self, function, lower, upper, max_error, max_iterations):
        return self.method.solve(function, lower, upper, max_error, max_iterations)
    
    def set_method(self, new_method):
        self.method = new_method
