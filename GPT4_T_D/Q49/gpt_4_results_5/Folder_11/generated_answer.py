
def if_decimal_is_divisible(bin_str):
    num = int(bin_str, 2)
    fib_16 = 987  # 16th number in Fibonacci sequence
    if num % fib_16 == 0:
        return True
    else:
        return False
