
def if_decimal_is_divisible(binary_str):
    fib = [0, 1]
    while len(str(fib[-1])) < len(binary_str):
        fib.append(fib[-1] + fib[-2])
    if fib[98] == int(binary_str, 2):
        return True
    return False
