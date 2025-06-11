'''
Завдання 7. Використання методу Монте-Карло

Необхідно написати програму на Python, яка імітує велику кількість кидків кубиків, обчислює суми чисел, які випадають на кубиках, і визначає ймовірність кожної можливої суми.

Створіть симуляцію, де два кубики кидаються велику кількість разів. Для кожного кидка визначте суму чисел, які випали на обох кубиках. Підрахуйте, скільки разів кожна можлива сума (від 2 до 12) з’являється у процесі симуляції. Використовуючи ці дані, обчисліть імовірність кожної суми.

На основі проведених імітацій створіть таблицю або графік, який відображає ймовірності кожної суми, виявлені за допомогою методу Монте-Карло.

'''


import random
import matplotlib.pyplot as plt

# Кількість симуляцій
num_simulations = 1_000_000

# Словник для підрахунку кількості кожної суми
sum_counts = {i: 0 for i in range(2, 13)}

# Симуляція кидків кубиків
for _ in range(num_simulations):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    sum_counts[total] += 1

# Обчислення ймовірностей методом Монте-Карло
monte_carlo_probabilities = {s: count / num_simulations * 100 for s, count in sum_counts.items()}

# Аналітичні ймовірності (в %)
theoretical_probabilities = {
    2: 2.78,
    3: 5.56,
    4: 8.33,
    5: 11.11,
    6: 13.89,
    7: 16.67,
    8: 13.89,
    9: 11.11,
    10: 8.33,
    11: 5.56,
    12: 2.78
}

# Вивід результатів
print(f"{'Сума':^5} | {'Монте-Карло (%)':^18} | {'Аналітична (%)':^18}")
print("-" * 50)
for s in range(2, 13):
    print(f"{s:^5} | {monte_carlo_probabilities[s]:^18.2f} | {theoretical_probabilities[s]:^18.2f}")

# Побудова графіку
sums = list(range(2, 13))
monte_carlo_values = [monte_carlo_probabilities[s] for s in sums]
theoretical_values = [theoretical_probabilities[s] for s in sums]

plt.figure(figsize=(10, 6))
plt.bar(sums, monte_carlo_values, width=0.4, label='Монте-Карло', align='center', alpha=0.7)
plt.plot(sums, theoretical_values, color='red', marker='o', label='Аналітична', linewidth=2)
plt.xlabel("Сума на кубиках")
plt.ylabel("Імовірність (%)")
plt.title("Ймовірність сум при киданні двох кубиків")
plt.legend()
plt.grid(True)
plt.xticks(sums)
plt.tight_layout()
plt.show()

'''
Програма:
Виконує 1 000 000 кидків двох шестигранних кубиків.
Підраховує, скільки разів випала кожна сума від 2 до 12.
Обчислює ймовірність появи кожної суми.
Виводить порівняння з аналітичними ймовірностями.
Будує графік для наочного порівняння.
'''