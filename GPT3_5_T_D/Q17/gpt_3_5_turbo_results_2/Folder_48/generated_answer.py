
def all_ints_div_by_both_two_nums(nums):
    result = []
    for num in nums[306:958]:
        if num % 982 == 0 and num % 319 == 0:
            result.append(num)
    return result
