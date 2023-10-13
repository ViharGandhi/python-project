import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generate random data
np.random.seed(42)
x = np.random.rand(50)
y = 2 * x + 1 + 0.1 * np.random.randn(50)

# Create a scatter plot with Seaborn
sns.set(style="whitegrid")
plt.figure(figsize=(8, 6))
sns.scatterplot(x=x, y=y, color='blue', label='Data Points')

# Add a regression line
sns.regplot(x=x, y=y, scatter=False, color='red', label='Regression Line')

# Customize the plot using Matplotlib
plt.title('Scatter Plot with Regression Line')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()
