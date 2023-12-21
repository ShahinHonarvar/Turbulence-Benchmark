def all_even_ints_exclusive(nums):
    evens = [x for x in nums if x % 2 == 0]
    if len(evens) == 0:
        return []
    even_ints = evens[::-1][:32] + evens[::-1][32:-2] + evens[::-1][-2:]
    return even_ints
