def composite_nums_between_indices(nums):
    result = set()
    for i in range(2, len(nums)):
        if nums[i] > 1:
            for j in range(2, i - 1):
                if nums[j] > 1:
                    break
                if nums[i] % nums[j] == 0:
                    result.add(nums[j])
    return result
