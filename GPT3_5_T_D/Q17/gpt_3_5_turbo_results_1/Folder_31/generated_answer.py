
def all_ints_div_by_both_two_nums(nums):
    result = []
    for num in nums[56:89]:
        if num % -59 == 0 and num % -79 == 0:
            result.append(num)
    return result
