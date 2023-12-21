
def if_decimal_is_divisible(binary):
    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            fib_seq = [0, 1]
            while len(fib_seq) <= n:
                fib_seq.append(fib_seq[-1] + fib_seq[-2])
            return fib_seq[n]

    decimal = int(binary, 2)
    fibonacci_97 = fibonacci(97)

    if decimal % fibonacci_97 == 0:
        return True
    else:
        return False
