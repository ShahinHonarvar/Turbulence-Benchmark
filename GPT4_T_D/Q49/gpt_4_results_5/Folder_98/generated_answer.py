
def if_decimal_is_divisible(binary_string):
    fibonacci_nums = [0, 1]
    for i in range(2, 14):
        fibonacci_nums.append(fibonacci_nums[i - 1] + fibonacci_nums[i - 2])
    decimal_integer = int(binary_string, 2)
    return decimal_integer % fibonacci_nums[13] == 0
