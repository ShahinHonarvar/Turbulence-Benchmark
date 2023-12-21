
def if_decimal_is_divisible(binary_str):
    decimal_int = int(binary_str, 2)
    fib_nums = [0, 1]
    while len(fib_nums) < 126:
        fib_nums.append(fib_nums[-1] + fib_nums[-2])
    
    if decimal_int % fib_nums[-1] == 0:
        return True
    else:
        return False
