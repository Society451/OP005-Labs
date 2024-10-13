import matplotlib.pyplot as plt
import numpy as np

# Data for 3ft
trial_3ft = [0.385, 0.381, 0.422, 0.399, 0.397, 0.427]
average_3ft = np.mean(trial_3ft)

# Data for 4ft
trial_4ft = [0.439, 0.553, 0.524, 0.451, 0.472, 0.501]
average_4ft = np.mean(trial_4ft)

# Data for 5ft
trial_5ft = [0.566, 0.521, 0.582, 0.579, 0.526, 0.538]
average_5ft = np.mean(trial_5ft)

# Combine the average times
averages = [average_3ft, average_4ft, average_5ft]
heights = ['3 ft', '4 ft', '5 ft']

# Create the plot
plt.figure(figsize=(10, 6))
plt.bar(heights, averages, color=['blue', 'orange', 'green'], alpha=0.7)

# Add labels and title
plt.title('Average Fall Times for Different Heights')
plt.xlabel('Height (ft)')
plt.ylabel('Average Time (s)')
plt.ylim(0, 0.6)  # Set limit for y-axis
plt.grid(axis='y')

# Display the average times on top of the bars
for i, avg in enumerate(averages):
    plt.text(i, avg + 0.01, f'{avg:.3f}s', ha='center')

# Show the plot
plt.tight_layout()
plt.show()
