import pandas as pd
import seaborn # Data visualization library based on matplotlib
import matplotlib.pyplot as plt
from vega_datasets import data

cars = data.cars()
cars = cars[['Acceleration', 'Cylinders', 'Displacement', 'Horsepower', 'Miles_per_Gallon', 'Weight_in_lbs']]
# print(cars.corr())
plt.figure(figsize=(8,8))
seaborn.heatmap(cars.corr(), annot=True, cmap="plasma").set_title('Co-Relation')
plt.tight_layout()
plt.show()
