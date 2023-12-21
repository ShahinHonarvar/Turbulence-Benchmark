
def all_ints_div_by_both_two_nums(nums):
    result = []
    for num in nums[73:86]:
        if num % 54 == 0 and num % 82 == 0:
            result.append(num)
    return result
