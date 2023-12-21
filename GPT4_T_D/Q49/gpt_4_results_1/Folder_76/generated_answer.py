
def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibo_nums = [0, 1]
    i = 1
    while len(fibo_nums) < 188:
        fibo_nums.append(fibo_nums[i-1] + fibo_nums[i])
        i += 1
    if decimal % fibo_nums[-1] == 0:
        return True
    else:
        return False
