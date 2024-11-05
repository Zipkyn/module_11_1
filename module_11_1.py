import numpy as np

arr = np.arange(1, 11)

squared = arr ** 2
sqrt_arr = np.sqrt(arr)
sum_arr = np.sum(arr)

print("Исходный массив:", arr)
print("Возведение в квадрат:", squared)
print("Квадратный корень:", sqrt_arr)
print("Сумма элементов массива:", sum_arr)

import pandas as pd

df = pd.read_csv('data.csv')

average = df['column_name'].mean()
median = df['column_name'].median()
filtered_data = df[df['column_name'] > 50]

print("Среднее значение:", average)
print("Медиана:", median)
print("Отфильтрованные данные:\n", filtered_data)

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))
plt.plot(df['x_column'], df['y_column'], label='Line Graph')
plt.scatter(df['x_column'], df['y_column'], color='red', label='Data Points')
plt.title("График зависимости")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()








