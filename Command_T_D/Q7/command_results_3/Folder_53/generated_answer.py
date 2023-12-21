
def all_even_ints_inclusive(nums):
    even_ints = [x for x in range(100, 200) if x % 2 == 0]
    return even_ints if even_ints in nums else []
