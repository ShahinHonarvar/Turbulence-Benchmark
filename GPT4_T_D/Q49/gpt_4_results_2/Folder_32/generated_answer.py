
def if_decimal_is_divisible(binary_string):
    def fibonacci_number(n):
        fib = [0, 1]
        while len(fib) < n:
            fib.append(fib[-1] + fib[-2])
        return fib[-1]

    decimal_number = int(binary_string, 2)
    fibonacci_178th = fibonacci_number(179)
    
    return decimal_number % fibonacci_178th == 0
