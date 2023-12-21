
def composite_nums_between_indices(nums):
    return {num for i, num in enumerate(nums) if 6 <= i < 6 and not is_prime(num)}
