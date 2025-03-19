import numpy as np
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

#__________________________________________________________________________

group_intervals = [14, 23, 32, 41, 50, 59, 68, 77]
group_freq = [4811, 9476, 7243, 7951, 1140, 1472, 330]

print(un_val)
print(freq)
def meana(values): #среднее
    return sum(values) / len(values)

group_un_val = []
group_freq = []
group_variances = [] #отклонения
for i in range(len(group_intervals) - 1):
    suma = 0 #cумма
    sum_freq = 0 #сумма частот
    group_variance_sum = 0 #группы вариаций сумм
    for j in range(len(un_val)):
        age = un_val[j]
        fre = freq[j]
        if group_intervals[i] <= age < group_intervals[i + 1]:
            suma+= age * fre
            sum_freq += fre
    group_mean = suma/sum_freq
    group_un_val.append(group_mean)
    group_freq.append(sum_freq)

    for j in range(len(un_val)):
        age = un_val[j]
        fre = freq[j]
        if group_intervals[i] <= age < group_intervals[i + 1]:
            group_variance_sum += (age - group_mean) ** 2 * fre
    group_variance = group_variance_sum / sum_freq
    group_variances.append(group_variance)

n_total = sum(group_freq)

overall_mean = sum(group_un_val[i] * group_freq[i] for i in range(len(group_un_val))) / n_total

print(sum(group_freq))


# Внутригрупповая дисперсия D_внгр по формуле (2.2)
D_within = sum(group_variances[i] * group_freq[i] for i in range(len(group_variances))) / n_total

# Межгрупповая дисперсия D_межгр по формуле (2.3)
D_between = sum(group_freq[i] * (group_un_val[i] - overall_mean) ** 2 for i in range(len(group_un_val))) / n_total

# Общая дисперсия D_общ по формуле (2.4) (проверка теоремы)
D_total = D_within + D_between

print("Групповые средние:", group_un_val)
print("Общая средняя:", overall_mean)
print("Групповые дисперсии:", group_variances)
print("Внутригрупповая дисперсия D_внгр:", D_within)
print("Межгрупповая дисперсия D_межгр:", D_between)
print("Общая дисперсия D_общ:", D_total)
print("Корреляционное отношение", math.sqrt(D_between/D_total))