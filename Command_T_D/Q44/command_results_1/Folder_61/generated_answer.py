def composite_nums_between_indices(nums):
    return set(nums) & {num for num in range(1, 8) if all(num % d != 0 for d in range(2, int(num ** .5) + 1))
