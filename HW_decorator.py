from functools import wraps

# ЗАДАЧА-1
# Написать свой декоратор который будет проверять остаток от деления числа 100 на результат работы функции ниже.
# Если остаток от деления = 0, вывести сообщение "We are OK!», иначе «Bad news guys, we got {}» остаток от деления.


def division_remainder(func):
    @wraps(func)
    def wrapper(*args):
        func_result = func(*args)
        result = 100 % func_result
        if result:
            message = f'Bad news guys, we got {result}'
        else:
            message = f'We are OK!'
        return message
    return wrapper

# ЗАДАЧА-2
# Написать декоратор который будет выполнять предпроверку типа аргумента который передается в вашу функцию.
# Если это int, тогда выполнить функцию и вывести результат, если это str(),
# тогда зарейзить ошибку ValueError (raise ValueError(“string type is not supported”))


def check_type_of_args(func):
    @wraps(func)
    def wrapper(*args):
        result = ''
        if type(*args) is str:
            raise ValueError('string type is not supported')
        if type(*args) is int:
            result = func(*args)
        return result
    return wrapper


# ЗАДАЧА-3
# Написать декоратор который будет кешировать значения аргументов и результаты работы вашей функции и записывать
# его в переменную cache. Если аргумента нет в переменной cache и функция выполняется, вывести сообщение
# «Function executed with counter = {}, function result = {}» и количество раз сколько эта функция выполнялась.
# Если значение берется из переменной cache, вывести сообщение «Used cache with counter = {}» и
# количество раз обращений в cache.

def repeat(number):
    def cache_args_result(func):
        @wraps(func)
        def wrapper(*args):
            cache = {}
            for num in range(number):
                if args in cache:
                    print(f'Used cache with counter = {num}')

                else:
                    cache.update({args: func(*args)})
                    print(f'Function executed with counter = {num}, function result = {cache[args]}')

            return f'\nThe function was executed {number} times'
        return wrapper
    return cache_args_result


@division_remainder
def exp_two(num):
    return num ** 2


print(exp_two(6))


@check_type_of_args
def exp_two(num):
    return num ** 2


print(exp_two(21))


@repeat(6)
def exp_two(num):
    return num ** 2


print(exp_two(4))
