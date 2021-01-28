import random


# 1) Сгенерировать dict() из списка ключей ниже по формуле (key : key* key). keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# ожидаемый результат: {1: 1, 2: 4, 3: 9 …}

keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dict_ = {key: key * key for key in keys}
print(dict_)
print("=" * 60)

# =======================================================
# 2) Сгенерировать массив(list()). Из диапазона чисел от 0 до 100 записать в результирующий массив только четные числа.

list1 = [x for x in range(0, 100, 2)]
list2 = [x for x in range(0, 100) if x % 2 == 0]
print(list1)
print("=" * 60)
print(list2)
print("=" * 60)

# =======================================================
# 3)Заменить в произвольной строке согласные буквы на гласные.


def change_consonant(line):
    vowels = 'aeyuioj'
    result = ''
    for letter in line:
        if letter not in vowels:
            result += random.choice(vowels)
        else:
            result += letter
    return result


text = 'hgetry nfgtreju'
print(change_consonant(text))
print("=" * 60)

# =======================================================
# 4)Дан массив чисел. [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
# 4.1) убрать из него повторяющиеся элементы

numbers = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
list_ = list(set(numbers))
print(list_)
print("=" * 60)

# =======================================================
# 4.2) вывести 3 наибольших числа из исходного массива
list_1 = numbers[:]
n = 0
max_numbers = []
while n < 3:
    max_n = max(list_1)
    max_numbers.append(max_n)
    list_1.remove(max_n)
    n += 1
print(max_numbers)


n = 0
max_numbers = []
while n < 3:
    max_n = max(list_)
    max_numbers.append(max_n)
    list_.remove(max_n)
    n += 1
print(max_numbers)
print("=" * 60)

# =======================================================
# 4.3) вывести индекс минимального элемента массива

print(numbers.index(min(numbers)))
print("=" * 60)

# =======================================================
# 4.4) вывести исходный массив в обратном порядке

print(numbers[::-1])
numbers.reverse()
print(numbers)
print("=" * 60)

# =======================================================
# 5) Найти общие ключи в двух словарях:

dict_one = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dict_two = {'a': 6, 'b': 7, 'z': 20, 'x': 40}
for i in dict_one:
    for j in dict_two:
        if j == i:
            print(j)
print("=" * 60)

# =======================================================
# 6)Дан массив из словарей
data = [
    {'name': 'Viktor', 'city': 'Kiev', 'age': 30},
    {'name': 'Maksim', 'city': 'Dnepr', 'age': 20},
    {'name': 'Vladimir', 'city': 'Lviv', 'age': 32},
    {'name': 'Andrey', 'city': 'Kiev', 'age': 34},
    {'name': 'Artem', 'city': 'Dnepr', 'age': 50},
    {'name': 'Dmitriy', 'city': 'Lviv', 'age': 21}]
# 6.1) отсортировать массив из словарей по значению ключа ‘age'

data_sort_age = sorted(data, key=lambda key: key['age'])
for d in data_sort_age:
    print(d)
print("=" * 60)

# =======================================================
# 6.2) сгруппировать данные по значению ключа 'city'
# вывод должен быть такого вида :
# result = {
#    'Kiev': [
#       {'name': 'Viktor', 'age': 30 },
#       {'name': 'Andrey', 'age': 34}],
#
#    'Dnepr': [ {'name': 'Maksim', 'age': 20 },
#               {'name': 'Artem', 'age': 50}],
#    'Lviv': [ {'name': 'Vladimir', 'age': 32 },
#              {'name': 'Dmitriy', 'age': 21}]
# }

result_ = {}
key = ''

for dict_ in data:
    list_value = []
    value = {}
    key = dict_['city']
    for k, v in dict_.items():
        if k != 'city':
            value[k] = v
    list_value.append(value)
    if key not in result_:
        result_.update({key: list_value})
    else:
        value_key = result_.get(key)
        value_key.append(list_value)
        result_.update({key: value_key})

print(result_)
print("=" * 60)

# =======================================================
# 7) У вас есть последовательность строк. Необходимо определить наиболее часто встречающуюся строку
# в последовательности. Например: most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'


def most_frequent(list_var):
    most_freq = None
    count_most_freq = 0
    for line in list_var:
        count_ = list_var.count(line)
        if count_ > count_most_freq:
            count_most_freq = count_
            most_freq = line
    return most_freq


print(most_frequent(['a', 'a', 'bi', 'bi', 'bi']))
print("=" * 60)

# =======================================================
# 8) Дано целое число. Необходимо подсчитать произведение всех цифр в этом числе, за исключением нулей.
# Например: Дано число 123405. Результат будет: 1*2*3*4*5=120.

num = input('input number: ')
res = 1
for i in num:
    if int(i):
        res *= int(i)
print(res)
print("=" * 60)

# =======================================================
# 9) Есть массив с положительными числами и число n (def some_function(array, n)).
# Необходимо найти n-ую степень элемента в массиве с индексом n. Если n за границами массива, тогда вернуть -1.


def some_function(array, n):
    if n <= (len(array) - 1):
        return array[n]**n
    else:
        return -1


array = [2, 5, 6, 4, 3, 1, 2]
print(some_function(array, 4))
print(some_function(array, 8))
print("=" * 60)


# =======================================================
# 10) Есть строка со словами и числами, разделенными пробелами (один пробел между словами и/или числами).
# Слова состоят только из букв. Вам нужно проверить есть ли в исходной строке три слова подряд.
# Для примера, в строке "hello 1 one two three 15 world" есть три слова подряд.
words = []
text = "hello 1 one two three 15 world"
for s in text.split():
    if s.isalpha():
        words.append(s)
        if len(words) == 3:
            print(*words)
            break
    else:
        del words[:]
else:
    print("not found")
# the end