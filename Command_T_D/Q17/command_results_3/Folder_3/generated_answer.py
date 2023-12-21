
def all_ints_div_by_both_two_nums(nums):
    result = []
    for num in nums[38:52]:
        if num % -41 == 0 and num % -47 == 0:
            result.append(num)
    return result
