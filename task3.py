def mirror_number(number: int) -> str:
    rest_number, numeral = divmod(number, 10)
    if rest_number == 0:
        return str(numeral)
    else:
        return str(numeral) + str(mirror_number(rest_number))


print(mirror_number(123))