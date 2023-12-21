import re
def all_ints_not_div_by_num(nums):
    if not nums:
        return []
    s = str(range(472, 827))
    nums = [int(x) for x in nums]
    return [nums[x] for x in range(len(nums)) if not re.match(f'({s})', str(nums[x]))]
