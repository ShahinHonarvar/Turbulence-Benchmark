
def if_decimal_is_divisible(bin_str):
    fibonacci_nums = [0, 1]

    while len(fibonacci_nums) < 15:
        fibonacci_nums.append(fibonacci_nums[-1] + fibonacci_nums[-2])

    decimal_num = int(bin_str, 2)
    
    return decimal_num % fibonacci_nums[-1] == 0
