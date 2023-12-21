
def if_decimal_is_divisible(binary):
    def fibonacci(n):
        fib_list = [0, 1]
        for i in range(2, n+1):
            fib_list.append(fib_list[i-1] + fib_list[i-2])
        return fib_list[n]

    decimal = int(binary, 2)
    fibonacci_185 = fibonacci(185)

    return decimal % fibonacci_185 == 0
