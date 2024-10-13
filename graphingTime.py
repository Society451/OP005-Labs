import matplotlib.pyplot as plt
import numpy as np

# Data for each height
heights = np.array([3, 4, 5])
average_times = np.array([0.382, 0.490, 0.552])  # Use previously calculated averages
std_devs = np.array([0.017, 0.042, 0.025])  # Use previously calculated std deviations

# Create the plot
plt.figure(figsize=(10, 6))

# Scatter plot
plt.scatter(heights, average_times, color='blue', label='Average Time (s)', s=100)

# Add error bars for standard deviation
plt.errorbar(heights, average_times, yerr=std_devs, fmt='o', color='black', capsize=5, label='Standard Deviation (s)')

# Add labels and title
plt.title('Average Fall Times and Standard Deviations for Different Heights')
plt.xlabel('Height (ft)')
plt.ylabel('Average Time (s)')
plt.ylim(0, 0.6)  # Set limit for y-axis
plt.grid(axis='y')

# Add legend
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()
