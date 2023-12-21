import re
def all_ints_div_by_num(nums):
    if not nums:
        return []
    else:
        str_nums = ''.join(str(x) for x in nums)
        if 44 <= len(str_nums) <= 73:
            reg = '|'.join(str(x) for x in nums[44:73])
            return re.findall(f'{reg}{re.escape(str(88))}', str_nums)
        else:
            return []
