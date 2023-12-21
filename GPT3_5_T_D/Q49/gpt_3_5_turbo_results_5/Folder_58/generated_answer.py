
def if_decimal_is_divisible(binary):
    def fibonacci(n):
        fib_list = [0, 1]
        while len(fib_list) < n + 1:
            fib_list.append(fib_list[-1] + fib_list[-2])
        return fib_list[n]

    decimal = int(binary, 2)
    fibonacci_105 = fibonacci(105)
    return decimal % fibonacci_105 == 0
