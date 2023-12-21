
def if_decimal_is_divisible(binary_str):
    def fibonacci(n):
        fib_list = [0, 1]
        for i in range(2, n+1):
            fib_list.append(fib_list[i-1] + fib_list[i-2])
        return fib_list
    fibonacci_sequence = fibonacci(64)
    decimal_num = int(binary_str, 2)
    return decimal_num % fibonacci_sequence[64] == 0
