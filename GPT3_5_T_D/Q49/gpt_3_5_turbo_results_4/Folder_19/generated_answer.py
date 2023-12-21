
def if_decimal_is_divisible(binary):
    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            fib_list = [0, 1]
            while len(fib_list) <= n:
                fib_list.append(fib_list[-1] + fib_list[-2])
            return fib_list[n]

    decimal = int(binary, 2)
    fibonacci_29 = fibonacci(29)
    return decimal % fibonacci_29 == 0
