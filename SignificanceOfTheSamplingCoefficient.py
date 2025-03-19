import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import math

# Исходный код
file_path = "Москва_2021.txt"
with open(file_path, 'r') as file:
    data = file.read().splitlines()

# Преобразуем данные в целые числа
data = list(map(int, data))

# Создаем дискретный ряд распределения
un_data = set(data)  # Уникальные значения
un_val = sorted(un_data)  # Сортируем уникальные значения
freq = [data.count(i) for i in un_val]  # Частоты для каждого уникального значения

# 1. Среднее для данных и для частот
mean_un_val = np.mean(un_val)  # Среднее значение для данных (x')
mean_freq = np.mean(freq)  # Среднее значение для частот (y')

# 2. Отклонения от среднего для данных и частот
deviations_un_val = [x - mean_un_val for x in un_val]  # Отклонения от среднего для данных (x-x')
deviations_freq = [f - mean_freq for f in freq]  # Отклонения от среднего для частот (y-y')

# 3. Сумма произведений отклонений
sum_of_products = sum([deviations_un_val[i] * deviations_freq[i] for i in range(len(freq))]) #сумма(x-x')(y-y')

# 4. Сумма квадратов отклонений для данных и частот
sum_of_squares_un_val = sum([dev ** 2 for dev in deviations_un_val])  # Для данных ..  сумма(x-x')^2
sum_of_squares_freq = sum([dev ** 2 for dev in deviations_freq])  # Для частот ..  сумма(y-y')^2

# 5. Коэффициент корреляции Пирсона
pearson_correlation = sum_of_products / np.sqrt(sum_of_squares_un_val * sum_of_squares_freq)
#_________________________________________________________
n = len(un_val)
T = pearson_correlation * math.sqrt(n - 2) / math.sqrt(1 - pearson_correlation ** 2)

alpha = 0.05 # уровень значимости
t_critical = stats.t.ppf(1 - alpha / 2, n - 2) # критическая точка

print(f"Значение T: {T}")
print(f"Критическое значение t: {t_critical}")

if abs(T) < t_critical:
    print("Нет оснований отвергать нулевую гипотезу: коэффициент корреляции незначим")
else:
    print("Нулевая гипотеза отвергается: выборочный коэффициент корреляции значимо отличается от нуля. Это означает, что величины X и Y коррелированы.")
