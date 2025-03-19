import numpy as np
import matplotlib.pyplot as plt

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

# Выводим коэффициент корреляции
print(f"Коэффициент корреляции Пирсона: {pearson_correlation:.3f}")
#_____________________________________________________________________

# Построим корреляционное поле (график разброса)
plt.figure(figsize=(8, 6))

# Построение графика разброса
plt.scatter(un_val, freq, color='purple', label='Данные')

# Настройка графика
plt.title("Корреляционное поле между уникальными значениями и их частотами")
plt.xlabel("Возраст (x)")
plt.ylabel("Частоты (y)")
plt.legend()

# Показать график
plt.grid(True)
plt.show()