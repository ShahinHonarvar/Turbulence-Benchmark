
def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_nums = [0, 1]
    i = 2
    while i < 190:
        fibonacci_nums.append(fibonacci_nums[i-1] + fibonacci_nums[i-2])
        i += 1
    return decimal % fibonacci_nums[-1] == 0
