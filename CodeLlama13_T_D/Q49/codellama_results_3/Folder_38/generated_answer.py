
def if_decimal_is_divisible(binary_string):
    binary_string = binary_string[::-1]
    n = 0
    for i, c in enumerate(binary_string):
        if c == "1":
            n += 2**i
    return (n % 78) == 0
