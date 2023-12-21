
def if_decimal_is_divisible(bin_str):
    fib = [0, 1]

    while len(fib) < 98:
        fib.append(fib[-1] + fib[-2])

    decimal = int(bin_str, 2)

    return decimal % fib[97] == 0
