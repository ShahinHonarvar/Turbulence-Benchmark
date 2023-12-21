
def all_ints_div_by_both_two_nums(numbers):
    divisible_by_both_nums = [num for num in numbers[86:91] if num % -71 == 0 and num % -67 == 0]
    return divisible_by_both_nums
