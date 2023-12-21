
def if_decimal_is_divisible(binary_string):
    fib = [0, 1]
    for i in range(2, 15):
        fib.append(fib[i-1] + fib[i-2])
    decimal = int(binary_string, 2)
    return decimal % fib[14] == 0
