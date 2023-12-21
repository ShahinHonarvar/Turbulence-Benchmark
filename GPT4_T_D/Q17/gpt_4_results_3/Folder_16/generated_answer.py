
def all_ints_div_by_both_two_nums(nums):
    result = []
    for num in nums[55:81]:
        if num % 22 == 0 and num % 32 == 0:
            result.append(num)
    return result
