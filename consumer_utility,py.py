import numpy as np
import matplotlib.pyplot as plt

# x = np.linspace(0, 1, 1000)

# # Logistic utility function
# def logistic_utility(x, x_0, coeff):
#     return 1 / (1 + np.exp(coeff * (x + x_0)))

# x_0_values = [-0.5]
# coeff_values = [-15]

# # Generate graphs for each combination
# for coeff in coeff_values:
#     for x_0 in x_0_values:
#         # Calculate utility values
#         y = logistic_utility(x, x_0, coeff)
        
#         # Plot the graph
#         plt.figure(figsize=(8, 5))
#         plt.plot(x, y, label=f"$x_0={x_0:.1f}$, Coeff={coeff}")
#         plt.title(f"Logistic Utility Function ($x_0={x_0:.1f}, Coeff={coeff}$)")
#         plt.xlabel("x")
#         plt.ylabel("Utility (y)")
#         plt.grid(True)
#         plt.legend()
#         plt.show()


def logistic_utility_bundle(x, coeff_A, coeff_B, x_0_A, x_0_B, theta):
    if x == 0:
        adjusted_x = 1 - x
        utility = 1 / (1 + np.exp(coeff_A * (adjusted_x + x_0_A)))
    elif x == 1:
        adjusted_x = x
        utility = 1 / (1 + np.exp(coeff_B * (adjusted_x + x_0_B)))
    else:
        utility = (1 + theta)*(1 / (1 + np.exp(coeff_A * (1-x + x_0_A))) + 1 / (1 + np.exp(coeff_B * (x + x_0_B))))
    return utility

x_0_A_range =  np.arange(-0.1, -1.1, -0.1)
coeff_A_range = np.arange(-5, -15, -1)
x_0_B_range = np.arange(-0.1, -1.1, -0.1)
coeff_B_range = np.arange(-5, -15, -1)

theta_values = [-0.1, -0.05, 0, 0.05, 0.1]
x_values = np.arange(0, 1.1, 0.1)

results = {}
for coeff_A in coeff_A_range:
    for coeff_B in coeff_B_range:
        for x_0_A in x_0_A_range:
            for x_0_B in x_0_B_range:
                for theta in theta_values:
                    key = (coeff_A, coeff_B, x_0_A, x_0_B, theta)
                    results[key] = [logistic_utility_bundle(x, coeff_A, coeff_B, x_0_A, x_0_B, theta) for x in x_values]


for coeff_A in coeff_A_range:
    for coeff_B in coeff_B_range:
        for x_0_A in x_0_A_range:
            for x_0_B in x_0_B_range:
                plt.figure(figsize=(10, 6))
                for theta in theta_values:
                    key = (coeff_A, coeff_B, x_0_A, x_0_B, theta)
                    utilities = results[key]
                    plt.plot(x_values, utilities, label=f"Theta={theta}")

                plt.title(f"Utility for coeff_A={coeff_A}, coeff_B={coeff_B}, x_0_A={x_0_A}, x_0_B={x_0_B}")
                plt.xlabel("x")
                plt.ylabel("Utility")
                plt.legend()
                plt.grid(True)
                plt.show()

