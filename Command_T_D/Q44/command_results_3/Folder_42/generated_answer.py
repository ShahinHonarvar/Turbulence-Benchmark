def composite_nums_between_indices(nums):
    return {x for x in range(91, 100) if all(x % d == 0 for d in range(2, int(x ** .5) + 1)) and x not in set(nums)}
