from RootSolver import RootSolver
from Methods import BisectionMethod
import math

function = lambda x: x**3 - 4
solver = RootSolver(BisectionMethod())
value, error = solver.solve(function, -3, 3, 0.001, 400)
print("Value is {val} with error {err}".format(val=value, err=error))
