from RootSolverMethods import RootSolver, BisectionMethod, RegulaFalsiMethod, SecantMethod
import math

function = lambda x: x**3 - 4
solver = RootSolver(BisectionMethod())
value, error = solver.solve(function, -3, 3, 0.001, 400)
print("Bisection Method")
print("Value is {val} with error {err}".format(val=value, err=error))
print("")

function = lambda x: x**3 - 4
solver = RootSolver(RegulaFalsiMethod())
value, error = solver.solve(function, -3, 3, 0, 1000)
print("Regula-Falsi Method")
print("Value is {val} with error {err}".format(val=value, err=error))
print("")

function = lambda x: x**3 - 4
solver = RootSolver(SecantMethod())
value, error = solver.solve(function, -3, 3, 0, 300000)
print("Secant Method")
print("Value is {val} with error {err}".format(val=value, err=error))
print("")
