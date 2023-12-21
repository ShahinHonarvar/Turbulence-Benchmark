import re
def all_ints_not_div_by_num(nums):
    result = []
    for num in nums[199:201]:
        if not re.match(r'0{3}(200){1}', str(num)):
            result.append(num)
    return result
