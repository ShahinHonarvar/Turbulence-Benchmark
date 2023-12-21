
def if_decimal_is_divisible(binary_string):
    fib = [0, 1]
    while len(fib) < 115:
        fib.append(fib[-1] + fib[-2])
    decimal = int(binary_string, 2)
    return decimal % fib[114] == 0
