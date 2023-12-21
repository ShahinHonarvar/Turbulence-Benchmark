def composite_nums_between_indices(nums):
    start, stop = 2, 2
    for i in range(2, len(nums)):
        if not nums[i]:
            start = i
            break
    for j in range(start, stop):
        if not nums[j]:
            stop = j
            break
    return set(nums[start:stop])
