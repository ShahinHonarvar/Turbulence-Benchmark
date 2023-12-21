def composite_nums_between_indices(nums):
    result = set()
    for num in nums[639:975]:
        if all(num % k != 0 for k in range(1, int(num ** .5) + 1)):
            result.add(num)
    return result
