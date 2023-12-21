
def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n+1:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[n]

def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fib_139 = fibonacci(139)
    if decimal % fib_139 == 0:
        return True
    else:
        return False
