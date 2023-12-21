
def all_ints_div_by_both_two_nums(nums):
    divisible_ints = []
    for num in nums[81:87]:
        if num % -33 == 0 and num % -62 == 0:
            divisible_ints.append(num)
    return divisible_ints
