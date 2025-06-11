'''
Завдання 6. Жадібні алгоритми та динамічне програмування

Необхідно написати програму на Python, яка використовує два підходи — жадібний алгоритм та алгоритм динамічного програмування для розв’язання задачі вибору їжі з найбільшою сумарною калорійністю в межах обмеженого бюджету.

Кожен вид їжі має вказану вартість і калорійність. Дані про їжу представлені у вигляді словника, де ключ — назва страви, а значення — це словник з вартістю та калорійністю.

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

Розробіть функцію greedy_algorithm жадібного алгоритму, яка вибирає страви, максимізуючи співвідношення калорій до вартості, не перевищуючи заданий бюджет.

Для реалізації алгоритму динамічного програмування створіть функцію dynamic_programming, яка обчислює оптимальний набір страв для максимізації калорійності при заданому бюджеті.
'''


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

# Жадібний алгоритм
def greedy_algorithm(items, budget):
    # Обчислюємо співвідношення калорій до вартості
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)

    selected = []
    total_cost = 0
    total_calories = 0

    for name, info in sorted_items:
        if total_cost + info['cost'] <= budget:
            selected.append(name)
            total_cost += info['cost']
            total_calories += info['calories']

    return selected, total_cost, total_calories

# Динамічне програмування (подібне до задачі "рюкзака")

def dynamic_programming(items, budget):
    item_names = list(items.keys())
    n = len(item_names)

    # dp[i][b] — макс. калорій для перших i предметів при бюджеті b
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    # Побудова таблиці
    for i in range(1, n + 1):
        name = item_names[i - 1]
        cost = items[name]['cost']
        cal = items[name]['calories']

        for b in range(budget + 1):
            if cost <= b:
                dp[i][b] = max(dp[i - 1][b], dp[i - 1][b - cost] + cal)
            else:
                dp[i][b] = dp[i - 1][b]

    # Відновлення вибору
    b = budget
    selected = []
    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            name = item_names[i - 1]
            selected.append(name)
            b -= items[name]['cost']

    selected.reverse()
    total_calories = dp[n][budget]
    total_cost = sum(items[i]['cost'] for i in selected)
    return selected, total_cost, total_calories

# Приклад використання
budget = 100

print("=== Жадібний підхід ===")
greedy_selected, greedy_cost, greedy_cal = greedy_algorithm(items, budget)
print(f"Обрано: {greedy_selected}")
print(f"Загальна вартість: {greedy_cost}, Калорій: {greedy_cal}")

print("\n=== Динамічне програмування ===")
dp_selected, dp_cost, dp_cal = dynamic_programming(items, budget)
print(f"Обрано: {dp_selected}")
print(f"Загальна вартість: {dp_cost}, Калорій: {dp_cal}")