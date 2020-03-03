from RootSolverMethods import BisectionMethod, RegulaFalsiMethod
from SignChangesMethods import BruteForceMethod
import math

function = lambda x: x**3 - 4
solver = BisectionMethod(function)
value, error = solver.solve(-3, 3, max_error = 0, max_iterations = 400, verbose = False)
print("Bisection Method")
print("Value is {val} with error {err}".format(val=value, err=error))
print("Values get by iterations: {}".format(solver.get_iteration_values()[0:20]))
print("")

function = lambda x: x**3 - 4
solver = RegulaFalsiMethod(function)
value, error = solver.solve(-3, 3, max_error = 0, max_iterations = 400, verbose = False)
print("Regula-Falsi Method")
print("Value is {val} with error {err}".format(val=value, err=error))
print("Values get by iterations: {}".format(solver.get_iteration_values()[0:20]))
print("")

function = lambda x: x**3 - 4
splitter = BruteForceMethod(function)
sign_changes = splitter.solve(-3, 3, 600)
for pair in sign_changes:
    print("Sign Change in ({}, {})".format(pair[0], pair[1]))
print("")

function = lambda x: math.sin(x)
splitter = BruteForceMethod(function)
sign_changes = splitter.solve(-100, 100, 10000)
for pair in sign_changes:
    print("Sign Change in ({}, {})".format(pair[0], pair[1]))
print("")

print("Refining the first subinterval")
sign_changes = splitter.solve(sign_changes[0][0], sign_changes[0][1], 10000)
for pair in sign_changes:
    print("Sign Change in ({}, {})".format(pair[0], pair[1]))
print("")
