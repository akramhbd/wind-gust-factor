import math
import tkinter as tk
from tkinter import ttk


def calculate_and_display():
    # Retrieve input values from the user
    B = float(B_entry.get())
    L = float(L_entry.get())
    h = float(h_entry.get())
    V = float(V_entry.get())
    n1 = float(n1_entry.get())

    epsilon = 0.333
    alpha = 0.25
    b = 0.45
    z_min = 9.14
    c = 0.3
    g_Q = 3.4
    l = 97.54
    beta = 0.02
    g_v = 3.4

    z = max(0.6 * h, z_min)
    I_z = c * (10 / z) ** (1 / 6)
    L_z = (l * (z / 10) ** epsilon)
    Q = math.sqrt(1 / (1 + 0.63 * ((B + h) / L_z) ** 0.63))
    g_R = math.sqrt(2 * math.log(3600 * n1)) + (0.577 / (math.sqrt(2 * math.log(3600 * n1))))
    V_z = b * ((z / 10) ** alpha) * V
    N1 = (n1 * L_z) / V_z
    R_n = (7.47 * N1) / ((1 + 10.3 * N1) ** (5 / 3))

    eta_h = 4.6 * n1 * (h / V_z)
    eta_B = 4.6 * n1 * (B / V_z)
    eta_L = 15.4 * n1 * (L / V_z)

    R_h = (1 / eta_h) - (1 / (2 * eta_h ** 2)) * (1 - math.exp(-2 * eta_h))
    R_B = (1 / eta_B) - (1 / (2 * eta_B ** 2)) * (1 - math.exp(-2 * eta_B))
    R_L = (1 / eta_L) - (1 / (2 * eta_L ** 2)) * (1 - math.exp(-2 * eta_L))

    R = math.sqrt((1 / beta) * R_n * R_h * R_B * (0.53 + 0.47 * R_L))

    temp1 = (g_Q * Q) ** 2
    temp2 = (g_R * R) ** 2
    temp3 = math.sqrt(temp1 + temp2)
    temp4 = (1 + 1.7 * I_z * temp3) / (1 + 1.7 * g_v * I_z)

    G_f = 0.925 * temp4

    # Display the result or update a label in the GUI
    result_label.config(text=f"Gust Effect Factor: {G_f:.3f}")


# Create the main window
root = tk.Tk()
root.title("Gust Effect Factor Calculator")

# Create labels and entry widgets for input parameters
B_label = ttk.Label(root, text="Width of Building, B (m):")
B_entry = ttk.Entry(root)

L_label = ttk.Label(root, text="Length of Building, L (m):")
L_entry = ttk.Entry(root)

h_label = ttk.Label(root, text="Height of the Building, h (m):")
h_entry = ttk.Entry(root)

V_label = ttk.Label(root, text="Basic Wind Speed, V (m/sec):")
V_entry = ttk.Entry(root)

n1_label = ttk.Label(root, text="Natural Frequency, n1 (hz):")
n1_entry = ttk.Entry(root)

# Place labels and entry widgets in the grid
instructions_label = ttk.Label(root, text="This calculator is for 'Exposure Category A' only."
                                          "\n2% Damping is Considered."
                                          " © Md. Akram Hossain.")
instructions_label.grid(row=0, column=0, columnspan=2, pady=10)

B_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
B_entry.grid(row=1, column=1, padx=10, pady=5)

L_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
L_entry.grid(row=2, column=1, padx=10, pady=5)

h_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
h_entry.grid(row=3, column=1, padx=10, pady=5)

V_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")
V_entry.grid(row=4, column=1, padx=10, pady=5)

n1_label.grid(row=5, column=0, padx=10, pady=5, sticky="e")
n1_entry.grid(row=5, column=1, padx=10, pady=5)

# Create a button to trigger the calculation
calculate_button = ttk.Button(root, text="Calculate", command=calculate_and_display)
calculate_button.grid(row=6, column=0, columnspan=2, pady=10)

# Create a label to display the result
result_label = ttk.Label(root, text="")
result_label.grid(row=7, column=0, columnspan=2, pady=10)

# Run the main event loop
root.mainloop()
