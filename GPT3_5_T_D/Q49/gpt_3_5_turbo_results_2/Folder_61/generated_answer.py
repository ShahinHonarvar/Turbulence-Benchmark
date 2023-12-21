
def if_decimal_is_divisible(binary_string):
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

    decimal_integer = int(binary_string, 2)
    fibonacci_number = fibonacci(76)

    if decimal_integer % fibonacci_number == 0:
        return True
    else:
        return False
