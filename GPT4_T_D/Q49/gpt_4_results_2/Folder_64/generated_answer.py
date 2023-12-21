
def if_decimal_is_divisible(binary_str):
    binary = int(binary_str, 2)
    fib = [0, 1]
    for i in range(2, 10):
        fib.append(fib[-1]+fib[-2])
    return binary % fib[9] == 0
