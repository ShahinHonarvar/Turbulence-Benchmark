
def if_decimal_is_divisible(binary_str):
    decimal_num = int(binary_str, 2)
    fib_arr = [0, 1]

    while len(fib_arr) < 95:
        fib_arr.append(fib_arr[-1] + fib_arr[-2])

    return decimal_num % fib_arr[94] == 0
