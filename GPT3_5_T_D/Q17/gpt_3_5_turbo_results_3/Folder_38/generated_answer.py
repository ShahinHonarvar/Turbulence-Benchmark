
def all_ints_div_by_both_two_nums(nums):
    divisible_nums = []
    for num in nums[10:77]:
        if num % -40 == 0 and num % -12 == 0:
            divisible_nums.append(num)
    return divisible_nums
