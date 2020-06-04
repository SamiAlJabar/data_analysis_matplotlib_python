from matplotlib import pyplot as plt
import numpy as np
import csv
from collections import Counter

plt.style.use('fivethirtyeight')
print(plt.style.available)

with open ('data.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    language_counter = Counter()
    for row in csv_reader:
        language_counter.update(row['LanguagesWorkedWith'].split(';'))

languages = []
popularity = []

for item in language_counter.most_common(10):
    languages.append(item[0])
    popularity.append(item[1])

plt.barh(languages, popularity)
plt.title('10 Popular Programming Languages')
plt.xlabel('Number of people')
plt.legend()
plt.tight_layout()
plt.show()