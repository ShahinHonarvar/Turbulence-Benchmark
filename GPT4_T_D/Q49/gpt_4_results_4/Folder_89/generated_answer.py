
def if_decimal_is_divisible(bin_str):
    fibonacci_list = []

    a, b = 0, 1
    while len(fibonacci_list) < 126:
        fibonacci_list.append(a)
        a, b = b, a + b

    dec = int(bin_str, 2)
    return dec % fibonacci_list[125] == 0
