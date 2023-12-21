
def if_decimal_is_divisible(binary_string):
    decimal_num = int(binary_string, 2)
    fibo_nums = [0, 1]
    while len(fibo_nums) <= 4:
        fibo_nums.append(fibo_nums[-2] + fibo_nums[-1])
    return decimal_num % fibo_nums[4] == 0
