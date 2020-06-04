from matplotlib import pyplot as plt

## PLOT STYLE
plt.style.use('fivethirtyeight')
# plt.style.use('ggplot')

## DATA INITIALIZATION
## AGE OF DEVELOPERS
dev_ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
## AVERAGE SALARY OF ALL DEVELOPERS
dev_sal_y = [30500, 37732, 41247, 45372, 48876, 53850, 57287, 63016, 65998, 70003, 75370]
## AVERAGE SALARY OF JAVA DEVELOPERS
java_dev_sal_y = [32000, 37732, 43247, 46372, 49976, 53850, 56287, 60016, 63998, 69003, 72370]

plt.plot(dev_ages_x, dev_sal_y, label='All Developers')
plt.plot(dev_ages_x, java_dev_sal_y, label='JAVA Developers')
# plt.plot(dev_ages_x, dev_sal_y, color='k', label='All Developers')
# plt.plot(dev_ages_x, java_dev_sal_y, color='b', linestyle='--', label='Python Developers')

## PLOT PROPERTIES
plt.title('Average Yearly Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Average Yearly Salary (USD)')
plt.legend()
plt.tight_layout()
# plt.grid(True)
plt.show()