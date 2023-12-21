
def if_decimal_is_divisible(binary_repr):
    decimal_number = int(binary_repr, 2)
    fib = [0, 1]
    for i in range(2, 13):
        fib.append(fib[i-1] + fib[i-2])
    if decimal_number % fib[12] == 0:
        return True
    else:
        return False
