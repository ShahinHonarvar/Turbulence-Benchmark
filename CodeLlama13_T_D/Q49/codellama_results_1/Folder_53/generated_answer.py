
def if_decimal_is_divisible(binary):
    num = int(binary, 2)
    fib = [0, 1]
    for i in range(2, 64):
        fib.append(fib[i-1] + fib[i-2])
    if num % fib[63] == 0:
        return True
    else:
        return False
