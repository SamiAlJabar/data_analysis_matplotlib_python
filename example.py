from matplotlib import pyplot as plt 

plt.style.use('classic')
print(plt.style.available)

temperature = [11, 21, 25, 12, 15, 13, 17, 19, 22, 14, 20, 23, 24, 18, 16]
price_of_icecream = [0.8, 4.5, 5.5, 0.8, 1.1, 1.0, 1.6, 2.0, 5.5, 1.1, 4.0, 5.5, 5.5, 2.0, 1.6]
price_of_jacket = [350, 100, 100, 350, 320, 350, 300, 250, 100, 320, 250, 100, 100, 250, 300]

for i in range(len(price_of_icecream)):
    price_of_icecream[i] = price_of_icecream[i] * 100

plt.scatter(temperature, price_of_icecream, color='blue', label='Ice Cream')
plt.scatter(temperature, price_of_jacket, color='black', label='Jacket')

plt.title('Temperature vs. Price')
plt.xlabel('Temperature')
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.show()