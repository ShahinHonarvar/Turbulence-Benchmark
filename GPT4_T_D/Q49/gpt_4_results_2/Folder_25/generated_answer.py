
def if_decimal_is_divisible(binary_string):
    number = int(binary_string, 2)

    def fibonacci(n):
        fib = [0, 1]
        while len(fib) < n + 1:
            fib.append(fib[-1] + fib[-2])
        return fib[n]
    
    return number % fibonacci(19) == 0
