import re
def all_odd_ints_inclusive(nums):
    if not nums:
        return []
    return re.findall(r'(odd)([0-9]+)', f'{str(639)}{str(nums)}{str(975)}')
