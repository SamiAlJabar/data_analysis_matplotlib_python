from matplotlib import pyplot as plt
import numpy as np

plt.style.use('fivethirtyeight')

dev_ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
x_ind = np.arange(len(dev_ages_x))
plt.xticks(ticks=x_ind, labels=dev_ages_x)
width=0.1

dev_sal_y = [30500, 37732, 41247, 45372, 48876, 53850, 57287, 63016, 65998, 70003, 75370]
java_dev_sal_y = [32000, 37732, 43247, 46372, 49976, 53850, 56287, 60016, 63998, 69003, 72370]


plt.bar(x_ind, dev_sal_y, width=width, color='k', label='All Developers')
plt.bar(x_ind + width, java_dev_sal_y, width=width, label='JAVA Developers')

## PLOT PROPERTIES
plt.title('Average Yearly Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Average Yearly Salary (USD)')
plt.legend()
plt.tight_layout()
# plt.grid(True)
plt.show()