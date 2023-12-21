
def if_decimal_is_divisible(binary_str):
    fibonacci_nums = [0, 1]
    while len(fibonacci_nums) < 75:
        next_num = fibonacci_nums[-1] + fibonacci_nums[-2]
        fibonacci_nums.append(next_num)
    
    decimal_num = int(binary_str, 2)
    return decimal_num % fibonacci_nums[73] == 0
