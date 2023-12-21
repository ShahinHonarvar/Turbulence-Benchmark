
def all_ints_div_by_both_two_nums(numbers):
    divisible_nums = []
    for num in numbers[281:695]:
        if num % -722 == 0 and num % -731 == 0:
            divisible_nums.append(num)
    return divisible_nums
