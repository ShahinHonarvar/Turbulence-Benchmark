
def if_decimal_is_divisible(bin_str):
    bin_num = int(bin_str, 2)
    fib_arr = [0, 1]
    for i in range(2, 176):
        fib_arr.append(fib_arr[i - 1] + fib_arr[i - 2])
    return bin_num % fib_arr[175] == 0
