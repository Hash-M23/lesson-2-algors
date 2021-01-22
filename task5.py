def ascii_print(start=32, string_n=1, end=127):
    if start < 0 or end > 127:
        return 
    string = f'{start} - {chr(start)}\n' if string_n % 10 == 0 else \
        f'{start} - {chr(start)} '
    if start == end:
        return string
    else:
        return string + ascii_print(start + 1, string_n + 1)


print(ascii_print())