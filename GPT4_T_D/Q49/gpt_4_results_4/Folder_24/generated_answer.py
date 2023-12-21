
def if_decimal_is_divisible(binary_string):
    def fibonacci(n):
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence[n-1]
    
    decimal_num = int(binary_string, 2)
    fibonacci_number = fibonacci(56)
    
    return decimal_num % fibonacci_number == 0
