import re
def all_ints_not_div_by_num(nums):
    if len(nums) < 3:
        return []
    output = []
    for i in range(2,len(nums)-1):
        if nums[i] % 8 != 0:
            output.append(nums[i])
            break
    return output
