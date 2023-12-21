
def if_decimal_is_divisible(binary_str):
    fib = [0, 1]
    while True:
        fib.append(fib[-1] + fib[-2])
        if len(fib) == 179:
            break
    decimal_int = int(binary_str, 2)
    if decimal_int % fib[-1] == 0:
        return True
    else:
        return False
