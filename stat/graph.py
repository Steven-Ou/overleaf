import matplotlib.pyplot as plt

# Data from your table (pic1.png)
flips = list(range(1, 11))
# Extracting the fractional results: 1/1, 1/2, 2/3, 2/4, 3/5, 3/6, 4/7, 4/8, 5/9, 6/10
relative_frequencies = [1/1, 1/2, 2/3, 2/4, 3/5, 3/6, 4/7, 4/8, 5/9, 6/10]

# Create the plot
plt.figure(figsize=(10, 5))

# Plot the data points and connecting lines
plt.plot(flips, relative_frequencies, color='black', marker='o', linewidth=2, markersize=8, label='Relative Frequency')

# Add the theoretical probability dashed line (0.5)
plt.axhline(y=0.5, color='black', linestyle='--', linewidth=1.5)

# Set axis limits to match your drawing
plt.xlim(0, 11)
plt.ylim(0, 1.1)

# Labeling axes to match your style
plt.xlabel('# of flips', loc='right', fontsize=12, fontweight='bold')
plt.ylabel('rel.\nfreq.', rotation=0, labelpad=20, loc='top', fontsize=12, fontweight='bold')

# Set tick marks
plt.xticks(range(0, 11))
plt.yticks([0.2, 0.4, 0.6, 0.8, 1.0], ['0.2', '0.4', '0.6', '0.8', '1'])

# Stylize the axes (Red lines like your drawing)
ax = plt.gca()
ax.spines['bottom'].set_color('red')
ax.spines['left'].set_color('red')
ax.spines['bottom'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Add a grid to mimic the graph paper
plt.grid(True, which='both', linestyle='-', linewidth=0.5, color='lightgray')

plt.tight_layout()
plt.show()