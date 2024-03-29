import math
import random

# https://github.com/qa-guru/qa_guru_python_5_4

def test_greeting():
    """
    Напишите программу, которая выводит на экран приветствие.
    """
    name = "Анна"
    age = 25
    # TODO Сформируйте нужную строку
    output = f"Привет, {name}! Тебе {age} лет."
    print(f"\n{output}")
    # Проверяем результат
    assert output == "Привет, Анна! Тебе 25 лет."


def test_rectangle():
    """
    Напишите программу, которая берет длину и ширину прямоугольника
    и считает его периметр и площадь.
    """
    a = 10
    b = 20

    # TODO сосчитайте периметр
    perimeter = 2*a + 2*b
    assert perimeter == 60

    # TODO сосчитайте площадь
    area = a*b
    assert area == 200


def test_circle():
    """
    Напишите программу, которая берет радиус круга и выводит на экран его длину и площадь.
    Используйте константу PI
    """
    r = 23
    # TODO сосчитайте площадь
    area = r ** 2 * math.pi
    print(f"\nПлощадь круга {area}")
    assert area == 1661.9025137490005

    # TODO сосчитайте длину окружности
    length = 2 * math.pi * r
    print(f"Длина окружности {length}")
    assert length == 144.51326206513048


def test_random_list():
    """
    Создайте список из 10 случайных чисел от 1 до 100 и отсортируйте его по возрастанию.
    """

    # TODO создайте список
    l = []
    for i in range(10):
        l.append(random.randint(1, 100))
    l.sort()
    assert len(l) == 10
    assert l[0] < l[-1]


def test_unique_elements():
    """
    Удалите из списка все повторяющиеся элементы
    """
    l = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]
    # TODO удалите повторяющиеся элементы
    l = list(set(l))
    assert isinstance(l, list)
    assert len(l) == 10
    assert l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # P.C. В лекции Сергей сказал, что set не работает со строками
    # на самом деле работает
    d = ["пятно", "собака", "пятно", "туча", "пятно", "собака"]
    e = ["туча", "собака", "конь"]

    f = list(set(d) & set(e))
    z = list(set(d) - set(e))
    d = list(set(d))
    print(f"\nСовпадающие значения строк в списках d и e {f}")
    print(f"Строки в d не совпадающие со строками в e {z}")
    print(f"Уникальные строки в списке d {d}")



def test_dicts():
    """
    Создайте словарь из двух списков.
    Используйте первый список как ключи, а второй - как значения.
    Выведите на экран все значения словаря.
    Подсказка: используй встроенную функцию zip.
    """
    first = ["a", "b", "c", "d", "e"]
    second = [1, 2, 3, 4, 5]
    # TODO создайте словарь
    d = dict(zip(first, second))
    print(f"\nСловарь {d}")

    assert isinstance(d, dict)
    assert len(d) == 5
