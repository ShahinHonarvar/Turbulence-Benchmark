
def all_ints_not_div_by_num(nums):
    result = []
    for num in nums[44:91]:
        if num % -68 != 0:
            result.append(num)
    return result
