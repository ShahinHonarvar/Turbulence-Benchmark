import re
def all_ints_not_div_by_num(nums):
    result = []
    for num in nums[36:85]:
        if not re.match(r"(-?\d+)", str(num)):
            continue
        elif int(str(num)) % -27 == 0:
            continue
        else:
            result.append(num)
    return result
