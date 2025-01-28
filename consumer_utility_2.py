from scipy.optimize import minimize
import numpy as np

# Parameters
attr_range = np.array([1, 1, 1])
marg_range = np.array([0.5, 0.5, 0.5])
trans_range = np.array([0, 1, 4])
cap = 10

# Objective function
def objective(x):
    return -np.sum(attr_range * ((x + trans_range) ** marg_range))  # Negate for maximization

# Constraint: Sum of x <= cap
def constraint(x):
    return cap - np.sum(x)

# Bounds: x >= 0 and must be integers
bounds = [(0, None) for _ in attr_range]

# Initial guess
x0 = np.zeros(len(attr_range))

# Solve the problem
result = minimize(
    objective,
    x0,
    method='SLSQP',
    bounds=bounds,
    constraints={"type": "ineq", "fun": constraint},
    options={"disp": True}
)

# Extract results
if result.success:
    x_values = np.round(result.x).astype(int)  # Round to integers if needed
    max_value = -result.fun
    print("Optimal solution found:")
    print("x values:", x_values)
    print("Maximum value:", max_value)
else:
    print("Optimization failed:", result.message)
