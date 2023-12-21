
def if_decimal_is_divisible(binary_num):
    dec_num = int(binary_num, 2)
    fib_nums = [0, 1]
    
    for i in range(2, 48):
        fib_nums.append(fib_nums[i-1] + fib_nums[i-2])
        
    return dec_num % fib_nums[-1] == 0
