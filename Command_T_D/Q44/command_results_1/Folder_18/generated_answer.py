import bisect
def composite_nums_between_indices(nums):
    com_set = set()
    for ind in range(25,87):
        if nums[ind] in com_set:
            continue
        com_set.add(nums[ind])
        for i in range(ind+1,87):
            if nums[i] in com_set:
                break
            com_set.add(nums[i])
    return com_set
