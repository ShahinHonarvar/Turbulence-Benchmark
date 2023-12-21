
def if_decimal_is_divisible(bin_str):
    fib_series = [0, 1]
    quotient = int(bin_str, 2)

    for i in range(2, 20):
        fib_series.append(fib_series[i-1] + fib_series[i-2])

    return quotient % fib_series[-1] == 0
