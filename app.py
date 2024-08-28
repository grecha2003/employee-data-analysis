import pandas as pd

# Загрузка данных из data.csv
data = pd.read_csv('data.csv')

# Вычисление средней зарплаты всех сотрудников
average_salary = data['salary'].mean()
print(f"Средняя зарплата всех сотрудников: {average_salary:.2f}")

# Отбор и вывод сотрудников, которым больше 30 лет
older_than_30 = data[data['age'] > 30]
print("\nСотрудники старше 30 лет:")
print(older_than_30)
