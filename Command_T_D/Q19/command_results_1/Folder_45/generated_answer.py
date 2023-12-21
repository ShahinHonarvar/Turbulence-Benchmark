def all_ints_not_div_by_num(nums):
    result = []
    for i in range(30, 200):
        if not nums[i] % -115:
            break
        result.append(nums[i])
    return result
