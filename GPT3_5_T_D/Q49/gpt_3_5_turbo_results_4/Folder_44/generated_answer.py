
def if_decimal_is_divisible(binary):
    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            fib_seq = [0, 1]
            for i in range(2, n+1):
                fib_seq.append(fib_seq[-1] + fib_seq[-2])
            return fib_seq[-1]
  
    decimal = int(binary, 2)
    fibonacci_159 = fibonacci(159)
  
    return decimal % fibonacci_159 == 0
