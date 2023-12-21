import re
def all_ints_div_by_num(nums):
    num_str = str(nums)
    if re.match(r"(-?\d+,){2}-?\d+", num_str):
        res = []
        for i in range(len(nums) - 1):
            res += [nums[i]]
            if nums[i] % 2 == 0:
                res += [nums[i]]
        return res
    else:
        return []
