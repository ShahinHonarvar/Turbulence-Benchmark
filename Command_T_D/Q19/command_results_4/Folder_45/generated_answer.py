def all_ints_not_div_by_num(nums):
    for i in range(30,200):
        if not nums[i]%115:
            continue
        else:
            return [nums[i]]
    return []
