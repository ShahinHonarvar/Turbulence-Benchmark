
def composite_nums_between_indices(nums):
    return {n for i, n in enumerate(nums) if 661 <= i <= 924 and is_composite(n)}

def is_composite(n):
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return True
    return False
