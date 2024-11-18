import matplotlib.pyplot as plt

# Provided data
kinetic = [0.026, 0.045, 0.065, 0.041, 0.0075, 0.053, 0.0767]
position_cm = [10, 25, 42.2, 60, 81.5, 102.5, 125.5]
potential = [0.090, 0.0618, 0.0403, 0.063, 0.096, 0.057, 0.023]

plt.figure(figsize=(8, 5))
plt.plot(position_cm, potential, marker='o', linestyle='-', color='b', label='Potential Energy')
plt.title('Potential Energy vs. Position')
plt.xlabel('Position (cm)')
plt.ylabel('Potential Energy (units)')
plt.grid(True)
plt.legend()
plt.show()


# Plotting the graph
plt.figure(figsize=(8, 5))
plt.plot(position_cm, kinetic, marker='o', linestyle='-', color='b', label='Kinetic Energy')
plt.title('Kinetic Energy vs. Position')
plt.xlabel('Position (cm)')
plt.ylabel('Kinetic Energy (units)')
plt.grid(True)
plt.legend()
plt.show()