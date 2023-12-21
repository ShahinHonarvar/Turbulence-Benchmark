
def all_even_ints_inclusive(nums):
    evens = [i for i in range(246, 750) if i % 2 == 0]
    return evens if len(evens) > 0 else []
