'''
Завдання 2. Рекурсія. Створення фрактала “дерево Піфагора” за допомогою рекурсії

Необхідно написати програму на Python, яка використовує рекурсію для створення фрактала “дерево Піфагора”. Програма має візуалізувати фрактал “дерево Піфагора”, і користувач повинен мати можливість вказати рівень рекурсії.
'''
import turtle

def draw_pythagorean_tree(length, angle, level, turtle_instance, color):
    if level is not None and length < level:
        return

    turtle_instance.color(color)
    turtle_instance.pensize(2)
    turtle_instance.forward(length)

    turtle_instance.left(angle)
    draw_pythagorean_tree(length * 0.7, angle, level, turtle_instance, color)
    turtle_instance.right(2 * angle)
    draw_pythagorean_tree(length * 0.7, angle, level, turtle_instance, color)
    turtle_instance.left(angle)
    turtle_instance.backward(length)

# Налаштування
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("white")
screen.title("Дерево Піфагора")

turtle = turtle.Turtle()
turtle.speed(0)  # Встановлюємо максимальну швидкість
turtle.penup()
turtle.left(90)
turtle.goto(-50, -150)
turtle.pendown()

# Налаштування
starting_length = 150
angle = 45
level = 10 # Глиьина рекурсії

# Запуск рекурсії
draw_pythagorean_tree(starting_length, angle, level, turtle, "blue")

screen.mainloop()

'''
Функція draw_pythagorean_tree() відповідає за рекурсивне малювання дерева.
Базовий випадок: якщо довжина відрізка стає занадто маленькою, рекурсію зупиняємо.
Рекурсивний крок:
Малюємо відрізок (за допомогою turtle.forward()).
Повертаємось вліво на заданий кут (turtle.left()).
Викликаємо функцію draw_pythagorean_tree() з новою довжиною та кутом для нового відрізка.
Повертаємось управо на подвійний кут (turtle.right()).
Викликаємо функцію draw_pythagorean_tree() для наступного відрізка.
Повертаємось вліво на заданий кут, щоб повернутись на попередній відрізок.
Відступаємо назад на довжину попереднього відрізка (turtle.backward()).
'''

