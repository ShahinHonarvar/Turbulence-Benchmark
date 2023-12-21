
def all_ints_div_by_both_two_nums(numbers):
    divisible_nums = []
    for num in numbers[22:25]:
        if num % -85 == 0 and num % -30 == 0:
            divisible_nums.append(num)
    return divisible_nums
