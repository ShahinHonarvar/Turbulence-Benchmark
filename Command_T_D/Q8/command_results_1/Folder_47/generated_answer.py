def all_even_ints_exclusive(nums):
    evens = [x for x in nums if x % 2 == 0]
    return evens[64:80] if len(evens) >= 64 else []
