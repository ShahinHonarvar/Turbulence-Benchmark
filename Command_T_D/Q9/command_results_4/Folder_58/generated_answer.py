import re
def all_odd_ints_inclusive(nums):
    return [i for i in range(209, 556) if re.search(r'(odd)', str(i), re.I)]
