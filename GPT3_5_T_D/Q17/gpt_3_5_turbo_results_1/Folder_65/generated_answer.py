
def all_ints_div_by_both_two_nums(nums):
    divisible_nums = []
    for num in nums[50:93]:
        if num % -94 == 0 and num % -95 == 0:
            divisible_nums.append(num)
    return divisible_nums
