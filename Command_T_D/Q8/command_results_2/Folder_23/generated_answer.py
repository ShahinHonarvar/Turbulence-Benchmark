def all_even_ints_exclusive(nums):
    even_ints = [n for n in nums if n % 2 == 0]
    if len(even_ints) == 0:
        return []
    return even_ints[29:53:2]
