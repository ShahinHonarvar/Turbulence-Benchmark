
def all_even_ints_inclusive(nums):
    even_ints = []
    for i in range(10, 66):
        if i % 2 == 0:
            even_ints.append(i)
    return even_ints
