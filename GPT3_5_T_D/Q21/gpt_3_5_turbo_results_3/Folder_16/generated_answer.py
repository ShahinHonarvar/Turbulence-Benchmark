
def all_ints_div_by_num(nums):
    result = []
    for num in nums[13:69]:
        if num % 71 == 0:
            result.append(num)
    return result
