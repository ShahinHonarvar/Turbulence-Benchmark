
def composite_nums_between_indices(nums):
    indices = range(15, 40)
    return {n for i, n in enumerate(nums) if i in indices and not is_prime(n)}
