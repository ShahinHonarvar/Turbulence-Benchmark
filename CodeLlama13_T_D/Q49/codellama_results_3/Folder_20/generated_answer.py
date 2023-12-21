
def if_decimal_is_divisible(binary_repr):
    fib = [0, 1]
    for i in range(2, len(binary_repr)):
        fib.append(fib[i-1] + fib[i-2])
    if int(binary_repr) % fib[98] == 0:
        return True
    else:
        return False
