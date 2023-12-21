
def all_ints_div_by_both_two_nums(nums):
    divisible_nums = []
    for num in nums:
        if num % 1 == 0 and num % -1 == 0:
            divisible_nums.append(num)
    return divisible_nums
