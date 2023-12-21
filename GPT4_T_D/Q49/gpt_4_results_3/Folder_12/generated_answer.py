
def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fib = [0, 1]
    for _ in range(2, 66):
        fib.append(fib[-1] + fib[-2])
    if decimal % fib[-1] == 0:
        return True
    return False
