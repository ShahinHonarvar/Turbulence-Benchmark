
def if_decimal_is_divisible(binary_string):
    def fibonacci(n):
        memo = {0: 0, 1: 1}
        if n not in memo:
            memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return memo[n]

    decimal_integer = int(binary_string, 2)
    fibonacci_185 = fibonacci(185)
    return decimal_integer % fibonacci_185 == 0
