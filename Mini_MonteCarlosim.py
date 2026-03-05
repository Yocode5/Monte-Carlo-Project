import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

def estimate_pi(n):

    x_axis = np.random.uniform(-1, 1, n)
    y_axis = np.random.uniform(-1, 1, n)

    inside_circle = x_axis**2 + y_axis**2 <= 1

    hits = inside_circle.sum()

    print(hits)

    pi = 4 * hits/n
    return pi

"""
print(estimate_pi(1000))
print(estimate_pi(10000))
print(estimate_pi(100000))

"""

df = pd.DataFrame(columns=["N", "Run", "Pi_Estimate"])

ns = [1000, 10000, 100000, 1000000]

for n in ns:

    for run in range(1, 11):
        pi_val = estimate_pi(n)
        df.loc[len(df)] = [n, run, pi_val]

print(df)

mean_vals = df.groupby("N")["Pi_Estimate"].mean()
print("\nMean values for each N:")
print(mean_vals)

def get_mode(s):
    return s.mode()[0]

mode_vals = df.groupby("N")["Pi_Estimate"].agg(get_mode)
print("\nMode values for each N:")
print(mode_vals)

summary_df = pd.DataFrame({
    "N": mean_vals.index,
    "Mean": mean_vals.values,
    "Mode": mode_vals.values
})

styled_runs = df.style.set_properties(
    **{
        "border": "1px solid",
        "text-align": "center"
    }
).set_table_styles([
    dict(selector="th", props=[("font-weight", "bold")])
])

styled_summary = summary_df.style.set_properties(
    **{
        "border": "1px solid #888",
        "text-align": "center"
    }
).set_table_styles([
    dict(selector="th", props=[("font-weight", "bold")])
])

timestamp = int(time.time())
file_name = f"Simulation_Results_{timestamp}.xlsx"

with pd.ExcelWriter(file_name, engine="openpyxl") as writer:
    styled_runs.to_excel(writer, sheet_name="Runs", index=False) 
    styled_summary.to_excel(writer, sheet_name="Summary", index=False)

print(f"Excel file Saved as {file_name} With Runs and Summary Sheets")

plt.figure(figsize=(8,5))

plt.plot(
    summary_df["N"],
    summary_df["Mean"],
    marker="o",
    linewidth=2,
    label="Estimated PI (Mean)"
)

plt.axhline(
    np.pi,
    color="red",
    linestyle="--",
    linewidth=1.8,
    label="Actual PI"
)

plt.xscale("log")

plt.xlabel("Number of Simulations (N)")
plt.ylabel("Estimated PI Value")
plt.title("Monte Carlo Estimation of PI vs Sample Size (N)")

plt.grid(True)
plt.legend()

plt.show()