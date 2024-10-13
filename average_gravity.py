# Constants
feet_to_meters = 0.3048

# Data for each height including all trial times
data = {
    '3ft': [0.485, 0.421, 0.429, 0.415, 0.431, 0.427],
    '4ft': [0.489, 0.553, 0.524, 0.451, 0.472, 0.501],
    '5ft': [0.566, 0.521, 0.582, 0.579, 0.526, 0.538]
}

# Distance in meters for each height
distances = {
    '3ft': 3 * feet_to_meters,
    '4ft': 4 * feet_to_meters,
    '5ft': 5 * feet_to_meters
}

# Calculate g for each trial and store results
results = {height: [] for height in data.keys()}

for height, times in data.items():
    D = distances[height]
    for t in times:
        g = (2 * D) / (t ** 2)
        results[height].append(g)

# Print results for each trial
for height, g_values in results.items():
    print(f"Gravitational accelerations for {height}:")
    for index, g in enumerate(g_values):
        print(f"  Trial {index + 1}: g = {g:.2f} m/s²")
    
    # Calculate and print the average value of g for each height
    average_g = sum(g_values) / len(g_values)
    print(f"Average g for {height}: {average_g:.2f} m/s²\n")
