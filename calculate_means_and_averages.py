import numpy as np

# Data for 3ft trials
trial_3ft = [0.385, 0.381, 0.422, 0.399, 0.397, 0.427]
average_3ft = np.mean(trial_3ft)
std_dev_3ft = np.std(trial_3ft)

# Data for 4ft trials
trial_4ft = [0.439, 0.553, 0.524, 0.451, 0.472, 0.501]
average_4ft = np.mean(trial_4ft)
std_dev_4ft = np.std(trial_4ft)

# Data for 5ft trials
trial_5ft = [0.566, 0.521, 0.582, 0.579, 0.526, 0.538]
average_5ft = np.mean(trial_5ft)
std_dev_5ft = np.std(trial_5ft)

# Print results
print(f"3 ft: Average = {average_3ft:.3f}s, Standard Deviation = {std_dev_3ft:.3f}s")
print(f"4 ft: Average = {average_4ft:.3f}s, Standard Deviation = {std_dev_4ft:.3f}s")
print(f"5 ft: Average = {average_5ft:.3f}s, Standard Deviation = {std_dev_5ft:.3f}s")
