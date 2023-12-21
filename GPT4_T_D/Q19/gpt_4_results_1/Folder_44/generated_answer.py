
def all_ints_not_div_by_num(nums):
    result = []
    for num in nums[47:91]:
        if num % 67 != 0:
            result.append(num)
    return result
