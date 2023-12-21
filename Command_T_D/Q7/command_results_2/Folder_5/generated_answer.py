
def all_even_ints_inclusive(nums):
    even_ints = [i for i in range(8, 10) if i % 2 == 0]
    return [x for x in nums if x in even_ints]
