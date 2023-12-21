def composite_nums_between_indices(nums):
    com = set()
    for i in range(74, 95+1):
        if not nums[i]%2 and not nums[i]%3 and not nums[i]%5:
            com.add(nums[i])
    return com
