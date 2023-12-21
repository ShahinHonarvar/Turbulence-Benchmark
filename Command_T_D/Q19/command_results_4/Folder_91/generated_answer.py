import re
def all_ints_not_div_by_num(nums):
    if not nums:
        return []
    str_nums = str(nums)
    for i in range(0, len(str_nums)):
        if str_nums[i] == '8':
            break
    str_nums = str_nums[:i] + str_nums[i+1:]
    return [int(num) for num in re.findall(r'\d+', str_nums)]
