import numpy as np
import matplotlib.pyplot as plt

# Parameters for the peaks
peak1 = -30
peak2 = 0
peak3 = 30

# Generate random data
num_samples = 10
noise_std = 5  # Adjust the noise level as needed

# Create random data around each peak
data1 = np.round(np.random.normal(loc=peak1, scale=noise_std, size=num_samples // 4))
data2 = np.round(np.random.normal(loc=peak2, scale=noise_std, size=num_samples // 2))
data3 = np.round(np.random.normal(loc=peak3, scale=noise_std, size=num_samples // 4))

# Combine the data
combined_data = np.concatenate([data1, data2, data3])

# Shuffle the data to make it random
np.random.shuffle(combined_data)

# Plot the histogram
plt.hist(combined_data, bins=50, density=True, alpha=0.6, color='b')
plt.xlabel("Value")
plt.ylabel("Density")
plt.title("Random Distribution with 3 Peaks (Integers)")
plt.grid(True)
plt.show()

print(combined_data)









































# import random


# class items_stuff:
    
#     alphabets_U = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     alphabets_L = alphabets_U.lower()

#     nums = "12345567890"

#     all_stuff = alphabets_L+alphabets_U+nums
#     # all_stuff = nums

#     def __init__(self) -> None:
#         self.posat = 0

#     def incrementpos(self):
#         self.posat += 1

#     def getitem(self):
#         self.posat += 1

#         if self.posat-1 >= len(items_stuff.all_stuff):
#             return False
#         else:
#             return items_stuff.all_stuff[self.posat-1]



