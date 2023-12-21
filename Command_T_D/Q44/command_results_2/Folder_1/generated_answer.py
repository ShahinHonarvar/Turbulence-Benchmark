def composite_nums_between_indices(nums):
    result = set()
    for i in range(69, 83):
        if i * i <= nums[-1]:
            result.update(list(range(i * i, nums[-1], i)))
    return result
