def calculator():
    operand = input('Введите  (+, -, *, / или 0 для выхода): ')

    if operand == '0':
        print('Вы вышли')

    else:
        if operand in ('+', '-', '*', '/'):
            num1 = int(input('Введите первое число: '))
            num2 = int(input('Введите второе число: '))

        if operand == '+':
            res = num1 + num2
            print(f'Сумма чисел равна:  {res}')
            return calculator()

        elif operand == '-':
            res = num1 - num2
            print(f'Разность чисел равна:  {res}')
            return calculator()

        elif operand == '*':
            res = num1 * num2
            print(f'Произведение чисел равно:  {res}')
            return calculator()

        elif operand == '/':
            if num2 == 0:
                print('Делитель не может быть равен 0')
                return calculator()
            else:
                res = num1 / num2
                print(f'Частное чисел равно:  {res}')
                return calculator()

        else:
            print('Данные введены некорректно')
            return calculator()


calculator()