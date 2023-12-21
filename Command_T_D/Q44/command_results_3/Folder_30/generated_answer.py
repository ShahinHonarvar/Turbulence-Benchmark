def composite_nums_between_indices(nums):
    result = set()
    for i in range(19, 93):
        if i not in result and nums[i] != 1:
            result.add(i)
            for j in range(2, int(nums[i] ** .5) + 1):
                if nums[i] % j == 0:
                    result.add(i * j)
                    result.add(i * (j + 1))
                    result.add(i * (j - 1))
                    break
    return result
