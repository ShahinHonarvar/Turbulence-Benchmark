
def if_decimal_is_divisible(binary_num):
    def fibonacci(n):
        fib_seq = [0, 1]
        for i in range(2, n+1):
            fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
        return fib_seq[n]
    
    decimal_num = int(binary_num, 2)
    fibonacci_199 = fibonacci(199)
    
    return decimal_num % fibonacci_199 == 0
