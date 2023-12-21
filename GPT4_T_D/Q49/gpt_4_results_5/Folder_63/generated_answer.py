
def if_decimal_is_divisible(bin_string):
    # convert binary string to decimal
    decimal = int(bin_string, 2)

    # fibonacci sequence generator
    def fibonacci(n):
        fib_series = [0, 1]
        while len(fib_series) < n:
            fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series[n - 1]

    # get the 144th fibonacci number
    fib_144th = fibonacci(144)

    # check if decimal is divisible by 144th fibonacci number
    return decimal % fib_144th == 0
