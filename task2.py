y = 0
x = 0


def count_numbers(number):
    global x, y

    if (number // 10) == 0:
        if number % 2 == 0:
            x += 1
        else:
            y += 1
        print(f'Количество четных цифр в числе: {x}, нечетных: {y}')
        return
    else:
        if (number % 10) % 2 == 0:
            x += 1
        else:
            y += 1
    return count_numbers(number // 10)


try:
    number = int(input('Введите натуральное число: '))
    count_numbers(number)
except ValueError:
    print('Данные введены некорректно')