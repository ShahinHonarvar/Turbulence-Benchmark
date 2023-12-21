import math
def all_ints_not_div_by_num(nums):
    for i in range(361, 887):
        if not nums[i] % 877:
            continue
        else:
            yield nums[i]
