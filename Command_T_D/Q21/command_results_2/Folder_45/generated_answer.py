import re
def all_ints_div_by_num(nums):
    # Your code here
    result = []
    for i in range(0, len(nums)):
        if nums[i] % 9 == 0:
            result.append(nums[i])
    return result
