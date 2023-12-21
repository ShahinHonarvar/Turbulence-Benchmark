
def if_decimal_is_divisible(bin_string):
    fib_arr = [0, 1]
    for _ in range(2, 128):
        fib_arr.append(fib_arr[-1] + fib_arr[-2])
    decimal = int(bin_string, 2)
    return decimal % fib_arr[127] == 0
