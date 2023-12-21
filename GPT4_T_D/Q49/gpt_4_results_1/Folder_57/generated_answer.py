
def fibonacci_index(n):
    fib = [0, 1]
    while len(fib) <= n:
        fib.append(fib[-1] + fib[-2])
    return fib[n]

def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fib_value = fibonacci_index(80)
    return decimal_value % fib_value == 0
