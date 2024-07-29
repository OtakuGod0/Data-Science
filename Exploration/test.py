import matplotlib.pyplot as plt
import numpy as np

# Define the target sum
target_sum = 10

# Generate the combinations where i + j = target_sum
combo = [(i, j) for i in range(10) for j in range(10) if i + j == target_sum]

# Group pairs by their sums
sum_groups = {}
for i, j in combo:
    s = i + j
    if s not in sum_groups:
        sum_groups[s] = []
    sum_groups[s].append((i, j))

# Create a colormap
cmap = plt.get_cmap('tab10', len(sum_groups))
color_map = {s: cmap(i) for i, s in enumerate(sum_groups)}

# Plot the pairs
plt.figure(figsize=(8, 8))

for s, pairs in sum_groups.items():
    x, y = zip(*pairs)
    plt.scatter(x, y, c=[color_map[s]] * len(pairs), label=f'Sum = {s}', s=100)

# Adding titles and labels
plt.title(f'Pairs with Sums up to {target_sum}')
plt.xlabel('X')
plt.ylabel('Y')
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.grid(True)
plt.legend()

# Show the plot
plt.show()
