
def all_ints_not_div_by_num(nums):
    result = []
    for num in nums[5:7]:
        if num % -6 != 0:
            result.append(num)
    return result
