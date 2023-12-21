
def all_ints_div_by_both_two_nums(nums):
    result = []
    for num in nums[29:54]:
        if num % -68 == 0 and num % -85 == 0:
            result.append(num)
    return result
