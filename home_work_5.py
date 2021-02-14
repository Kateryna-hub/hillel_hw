import string

'''
1)Из текстового файла удалить все слова, содержащие от трех до пяти символов,
но при этом из каждой строки должно быть удалено только четное количество таких слов.
'''


def list_extra_words(list_):
    """
    find all words containing from three to five characters,
    only an even number of such words should be found in the string.
    :param list_: list of words
    :return: list of words containing from three to five characters, an even number
    """
    extra_words = [word for word in list_ if 3 <= len(word) <= 5]
    count = 0
    for word_ in list_:
        if 3 <= len(word_) <= 5:
            count += 1
    if count % 2:
        extra_words.pop()
    return extra_words


with open('text.txt', 'r') as text_f:
    with open('text_new.txt', 'w') as new_text_f:
        for line in text_f.readlines():
            list_words = line.translate(str.maketrans(dict.fromkeys(string.punctuation))).split()
            delete_words = list_extra_words(list_words)
            new_line = [word for word in list_words if word not in delete_words]
            new_text_f.write(f'{" ".join(new_line)}\n')


'''
2)Текстовый файл содержит записи о телефонах и их владельцах. Переписать в другой файл телефоны тех владельцев,
фамилии которых начинаются с букв К и С.
'''

with open('phone.txt', 'r') as ph_file:
    with open('phone_new.txt', 'w') as new_file:
        for line in ph_file.readlines():
            surname = (line.split())[1]
            if surname[:1] in 'СК':
                new_file.write(line)


'''
3) Получить файл, в котором текст выровнен по правому краю путем равномерного добавления пробелов.
'''

with open('text.txt') as file1:
    with open('text_rjust.txt', 'w') as file2:
        for line in file1:
            file2.write(f'{line.rjust(120)}\n')

'''
4)Дан текстовый файл со статистикой посещения сайта за неделю. Каждая строка содержит ip адрес, 
время и название дня недели (например, 139.18.150.126 23:12:44 sunday). Создайте новый текстовый файл, 
который бы содержал список ip без повторений из первого файла. Для каждого ip укажите количество посещений, 
наиболее популярный день недели. Последней строкой в файле добавьте наиболее популярный отрезок времени в сутках 
длиной один час в целом для сайта.
'''


with open('visit_site.txt', 'r') as log:
    with open('visit_statistics.txt', 'w') as stat:
        list_item = [line.split() for line in log.read().split('\n')]
        list_ip = [ip[0] for ip in list_item]
        for ip in set(list_ip):
            stat.write(f'{ip} number of visits: {list_ip.count(ip)}\n')
        days_week = [day[2] for day in list_item]
        max_day = max(days_week, key=days_week.count)
        stat.write(f'the most popular day of the week: {max_day}\n')
        hours = [time[1].split(':')[0] for time in list_item]
        max_hour = max(hours, key=hours.count)
        stat.write(f'the most popular segment of time in a day: {max_hour}')
