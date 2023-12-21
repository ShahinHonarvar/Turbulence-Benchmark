
def if_decimal_is_divisible(binary_representation):
    def fibonacci(n):
        fib_series = [0, 1]
        while len(fib_series) < n:
            fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series[-1]

    number = int(binary_representation, 2)
    return number % fibonacci(68) == 0
