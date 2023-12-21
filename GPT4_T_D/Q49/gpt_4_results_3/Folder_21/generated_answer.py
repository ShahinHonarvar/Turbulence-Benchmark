
def if_decimal_is_divisible(binary_string):
    fib_nums = [0, 1]
    while len(fib_nums) < 196:
        fib_nums.append(fib_nums[-1] + fib_nums[-2])
    
    decimal_num = int(binary_string, 2)
    fib_195 = fib_nums[195]

    return decimal_num % fib_195 == 0  
