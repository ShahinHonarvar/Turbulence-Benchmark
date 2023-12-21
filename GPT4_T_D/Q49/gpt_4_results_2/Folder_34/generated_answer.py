
def if_decimal_is_divisible(bin_string):
    fib = [0, 1]
    for i in range(2, 24):
        fib.append(fib[i-1] + fib[i-2])
    dec_number = int(bin_string, 2)
    return dec_number % fib[23] == 0
