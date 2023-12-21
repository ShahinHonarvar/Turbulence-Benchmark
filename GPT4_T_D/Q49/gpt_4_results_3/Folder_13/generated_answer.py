
def if_decimal_is_divisible(bin_num):
    fib_series = [0, 1]
    dec_num = int(bin_num, 2)
    
    while len(fib_series) <= 174:
        fib_series.append(fib_series[-1] + fib_series[-2])
    
    return dec_num % fib_series[173] == 0
