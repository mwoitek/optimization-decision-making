# %%
import pulp as pl

# %%
# Decision variables
x1 = pl.LpVariable("x_1", lowBound=0, upBound=700)
x2 = pl.LpVariable("x_2", lowBound=0, upBound=700)
x3 = pl.LpVariable("x_3", lowBound=0, upBound=700)

# %%
# Define problem and add objective function
prob = pl.LpProblem("MedicalDeviceExample", pl.LpMinimize)
prob += 5 * x1 + 4 * x2 + 3 * x3

# %%
# Add remaining constraints
prob += 0.4 * x1 + 0.3 * x2 + 0.2 * x3 >= 500
prob += 0.4 * x1 + 0.35 * x2 + 0.2 * x3 >= 300
prob += 0.2 * x1 + 0.35 * x2 + 0.6 * x3 >= 300

# %%
# Solve the problem
prob.solve(pl.PULP_CBC_CMD(msg=False))
status = pl.LpStatus[prob.status]
assert status == "Optimal", "Could not find optimal solution"

# %%
# Print optimal solution
for i, x in enumerate([x1, x2, x3], start=1):
    print(f"x_{i} = {pl.value(x)}")

min_cost = pl.value(prob.objective)
print(f"Minimum cost: {min_cost}")

# x_1 = 700.0
# x_2 = 700.0
# x_3 = 50.0
# Minimum cost: 6450.0

# %%
# Number of large and small valves
opt_x1 = pl.value(x1)
opt_x2 = pl.value(x2)
opt_x3 = pl.value(x3)

assert isinstance(opt_x1, float)
assert isinstance(opt_x2, float)
assert isinstance(opt_x3, float)

num_large = 0.4 * opt_x1 + 0.3 * opt_x2 + 0.2 * opt_x3
num_small = 0.2 * opt_x1 + 0.35 * opt_x2 + 0.6 * opt_x3

print(f"Large valves: {num_large}")
print(f"Small valves: {num_small}")

# Large valves: 500.0
# Small valves: 415.0
