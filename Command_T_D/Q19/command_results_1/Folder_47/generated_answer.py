import bisect
def all_ints_not_div_by_num(nums):
    result = []
    if 25 <= len(nums) <= 76:
        for i in range(25, 76):
            if nums[i] % -53 != 0:
                result.append(nums[i])
        return result
    else:
        return []
