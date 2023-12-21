import re
def all_even_ints_exclusive(nums):
    if not nums:
        return []
    return [n for n in range(385,999,2) if n % 2 == 0 and str(n) in re.findall(r'\d+', nums)]
