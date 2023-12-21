
def if_decimal_is_divisible(binary_string):
    fib = [0, 1]
    while len(fib) < 160:
        fib.append(fib[-1] + fib[-2])
    num = int(binary_string, 2)
    if num % fib[159] == 0:
        return True
    else:
        return False
