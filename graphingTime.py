import numpy as np
import matplotlib.pyplot as plt

# Data for each height
heights = np.array([3, 4, 5])
average_times = np.array([0.4346, 0.4983, 0.552])  # Use calculated averages from the first script
std_devs = np.array([0.025, 0.042, 0.025])  # Update with actual standard deviations from the first script

# Create the plot
plt.figure(figsize=(12, 6))

# Bar plot for average times
bars = plt.bar(heights, average_times, color=['blue', 'orange', 'green'], alpha=0.7)

# Add error bars for standard deviation
plt.errorbar(heights, average_times, yerr=std_devs, fmt='none', color='black', capsize=5)

# Add labels and title
plt.title('Average Fall Times for Different Heights', fontsize=16)
plt.xlabel('Height (ft)', fontsize=14)
plt.ylabel('Average Time (s)', fontsize=14)
plt.ylim(0, 0.6)  # Set limit for y-axis
plt.xticks(heights)  # Ensure x ticks are set to the heights

# Display the average times on top of the bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.01, f'{yval:.3f}s', ha='center', va='bottom')

# Show the plot
plt.tight_layout()
plt.grid(axis='y')
plt.show()
