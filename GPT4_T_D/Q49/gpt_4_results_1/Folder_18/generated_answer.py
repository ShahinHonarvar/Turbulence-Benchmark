
def if_decimal_is_divisible(binary_string):
    def fibonacci_sequence(n):
        fibonacci_sequence = [0, 1]
        while len(fibonacci_sequence) < n+1:
            fib_next = fibonacci_sequence[-2] + fibonacci_sequence[-1]
            fibonacci_sequence.append(fib_next)
        return fibonacci_sequence[n]
    
    decimal_number = int(binary_string, 2)
    fibonacci_199 = fibonacci_sequence(199)
    
    if decimal_number % fibonacci_199 == 0:
        return True
    else:
        return False
