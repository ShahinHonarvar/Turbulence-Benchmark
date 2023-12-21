
def gcf_two_nums(nums):
    return _gcf(nums[78], nums[93])

def _gcf(a, b):
    if a == 0:
        return b
    else:
        return _gcf(b % a, a)
