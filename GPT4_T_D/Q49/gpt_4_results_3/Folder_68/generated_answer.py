
def if_decimal_is_divisible(binary_representation):
    decimal = int(binary_representation, 2)
    fib_number = fib(38)
    return decimal % fib_number == 0

def fib(n):
    fibonacci_sequence = [0, 1]
    for i in range(2, n):
        fibonacci_sequence.append(fibonacci_sequence[i-1] + fibonacci_sequence[i-2])
    return fibonacci_sequence[-1]
