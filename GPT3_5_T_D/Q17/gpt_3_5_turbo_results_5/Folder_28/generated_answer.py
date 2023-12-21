
def all_ints_div_by_both_two_nums(nums):
    divisible_nums = []
    for num in nums[34:82]:
        if num % 27 == 0 and num % 57 == 0:
            divisible_nums.append(num)
    return divisible_nums
