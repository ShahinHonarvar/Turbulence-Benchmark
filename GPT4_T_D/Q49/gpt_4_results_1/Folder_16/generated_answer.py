
def if_decimal_is_divisible(bin_str):
    bin_num = int(bin_str, 2)
    fib_numbers = [0, 1]
    for i in range(2, 128):
        fib_numbers.append(fib_numbers[i-1] + fib_numbers[i-2])
    return bin_num % fib_numbers[-1] == 0
