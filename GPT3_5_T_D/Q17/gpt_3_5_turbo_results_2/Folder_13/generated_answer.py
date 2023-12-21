
def all_ints_div_by_both_two_nums(nums):
    divisible_integers = []
    for i in range(13, 19):
        if nums[i] % 45 == 0 and nums[i] % 20 == 0:
            divisible_integers.append(nums[i])
    return divisible_integers
