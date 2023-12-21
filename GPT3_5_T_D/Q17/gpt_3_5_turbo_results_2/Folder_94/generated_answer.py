
def all_ints_div_by_both_two_nums(nums):
    divisible_nums = []
    for num in nums[93:95]:
        if num % -53 == 0 and num % -91 == 0:
            divisible_nums.append(num)
    return divisible_nums
