def all_neg_ints_exclusive(nums):
    negative_list = []
    for i in range(43, 99):
        if nums[i] < 0:
            negative_list.append(nums[i])
    return negative_list
