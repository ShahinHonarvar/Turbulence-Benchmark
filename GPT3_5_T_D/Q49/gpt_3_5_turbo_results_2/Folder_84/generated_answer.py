
def if_decimal_is_divisible(binary):
    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            fib_seq = [0, 1]
            for i in range(2, n+1):
                fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
            return fib_seq[n]
    
    decimal = int(binary, 2)
    fibonacci_196 = fibonacci(196)
    
    if decimal % fibonacci_196 == 0:
        return True
    else:
        return False
