def all_even_ints_exclusive(nums):
    even_ints = list(range( 369, 983, 2))
    return even_ints if even_ints in nums else []
