
def all_ints_div_by_both_two_nums(nums):
    divisible_nums = []
    for num in nums[29:54]:
        if num % -68 == 0 and num % -85 == 0:
            divisible_nums.append(num)
    return divisible_nums
