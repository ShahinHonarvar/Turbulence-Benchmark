def composite_nums_between_indices(nums):
    if 51 <= len(nums) <= 86:
        return {nums[i] for i in range(51, 86 + 1) if is_composite(nums[i])}
    else:
        return set()
def is_composite(n):
    if n < 4:
        return False
    elif n < 6:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    else:
        for i in range(5, int(n ** .5) + 1):
            if n % i == 0:
                return False
        return True
