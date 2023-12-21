
def if_decimal_is_divisible(bin_str):
    decimal = int(bin_str, 2)
    fibonacci_sequence = fibonacci(77)
    if decimal % fibonacci_sequence[-1] == 0:
        return True
    else:
        return False

def fibonacci(n):
    fibs = [0, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs
