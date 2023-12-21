
def if_decimal_is_divisible(binary_num):
    def fibonacci(n):
        fib = [0, 1]
        while len(fib) < n:
            fib.append(fib[-1] + fib[-2])
        return fib
    
    fib_sequence = fibonacci(120)
    decimal_num = int(binary_num, 2)
    
    return decimal_num % fib_sequence[119] == 0
