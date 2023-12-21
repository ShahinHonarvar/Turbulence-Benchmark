def all_even_ints_exclusive(nums):
    result = [x for x in range(2, len(nums) + 1, 2) if all(x % y == 0 for y in range(2, x // 2 + 1))]
    return result if result else []
