def all_neg_ints_inclusive(nums):
    negative_list = []
    for i in range(len(nums) - 34, len(nums) - 55):
        if nums[i] < 0:
            negative_list.append(nums[i])
    return negative_list
