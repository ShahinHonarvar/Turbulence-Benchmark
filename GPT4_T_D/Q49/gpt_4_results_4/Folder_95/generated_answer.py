
def if_decimal_is_divisible(bin_str):
    fib_nums = [0, 1]
    n = 168
    while len(fib_nums) < n + 1:
        fib_nums.append(fib_nums[-1] + fib_nums[-2])
    
    decimal_num = int(bin_str, 2)
    
    if decimal_num % fib_nums[n] == 0:
        return True
    else:
        return False
