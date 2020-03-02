from RootSolverMethods import BisectionMethod, RegulaFalsiMethod, SecantMethod
import math

function = lambda x: x**3 - 4
solver = BisectionMethod(function)
value, error = solver.solve(-3, 3, max_error = 0, max_iterations = 400, verbose = False)
print("Bisection Method")
print("Value is {val} with error {err}".format(val=value, err=error))
print("Values get by iterations: {}".format(solver.get_values()[0:20]))
print("")

