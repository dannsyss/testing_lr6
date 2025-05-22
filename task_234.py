# 1) Функция с делением на ноль
def f1(x):
    try:
        result = (x ** 2 + 3 * x + 2) / (x - 5)
        return result
    except ZeroDivisionError:
        print("Ошибка: Деление на ноль. Введите значение x, отличное от 5.")
        print(f"Попробуйте другое значение x. Например, для x=6 результат: {(6**2 + 3*6 + 2)/(6-5)}")
        return None
    except TypeError:
        print("Ошибка: Неправильный тип данных. Введите числовое значение.")
        return None


# 2) Функция с использованием необъявленной переменной
def f2(x, y):
    try:
        return x * y * z
    except NameError:
        print("Ошибка: Переменная z не определена. Определите переменную z перед вызовом функции.")
        return None
    except TypeError:
        print("Ошибка: Неправильный тип данных. Введите числовые значения для x и y.")
        return None


# 3) Функция подсчета символов в строке
def f3(s):
    try:
        return len(s)
    except TypeError:
        print("Ошибка: Функция ожидает строку. Введите строковое значение.")
        return None


# 4) Функция сравнения средних четных и нечетных чисел из sp1
def f4(numbers):
    even = [x for x in numbers if x % 2 == 0]
    odd = [x for x in numbers if x % 2 != 0]

    avg_even = sum(even) / len(even) if even else 0
    avg_odd = sum(odd) / len(odd) if odd else 0

    return "Четные" if avg_even > avg_odd else "Нечетные"


# 5) Функция с логической ошибкой
def f5(n):
    result = 1
    for i in range(n):
        result *= i
    return result


sp1 = [32604, 33049, 33494, 34289, 34734, 35179, 35624, 49419, 49864, 50309, 51104, 51549, 51994]

'''
print("Функция f1()")
print("f1(6):", f1(6))
print("f1(5):", f1(5))
print("f1('a'):", f1('a'))

print("\nФункция f2()")
print("f2(2, 3):", f2(2, 3))
print("f2('a', 'b'):", f2('a', 'b'))

print("\nФункция f3()")
print("f3('hello'):", f3('hello'))
print("f3(123):", f3(123))

print("\nФункция f4()")
print("f4(sp1):", f4(sp1))
print("f4([1, 3, 5]):", f4([1, 3, 5]))
print("f4([2, 4, 6]):", f4([2, 4, 6]))

print("\nФункция f5()")
print("f5(0):", f5(0))
print("f5(1):", f5(1))
print("f5(5):", f5(5))
'''

def logging_and_caching(func):
    cache = {}  # Словарь для кэширования результатов

    def wrapper(x):
        # Логирование вызова функции
        print(f"Вызов функции {func.__name__} с аргументом x = {x}")

        # Проверка наличия результата в кэше
        if x in cache:
            print("Результат взят из кэша")
            return cache[x]

        try:
            result = func(x)
            # Кэширование результата
            cache[x] = result
            print("Результат сохранен в кэш")
            return result
        except Exception as e:
            print(f"Произошла ошибка: {type(e).__name__} - {str(e)}")
            return None

    return wrapper


# Декоратор к функции f1
@logging_and_caching
def f1(x):
    try:
        result = (x ** 2 + 3 * x + 2) / (x - 5)
        return result
    except ZeroDivisionError:
        print("Ошибка: Деление на ноль. Введите значение x, отличное от 5.")
        print(f"Попробуйте другое значение x. Например, для x=6 результат: {(6 ** 2 + 3 * 6 + 2) / (6 - 5)}")
        return None
    except TypeError:
        print("Ошибка: Неправильный тип данных. Введите числовое значение.")
        return None


print("Первый вызов:")
print(f1(6))

print("\nВторой вызов с тем же аргументом:")
print(f1(6))

print("\nВызов с ошибкой:")
print(f1(5))