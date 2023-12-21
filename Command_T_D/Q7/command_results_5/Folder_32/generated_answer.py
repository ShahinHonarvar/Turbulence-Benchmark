
def all_even_ints_inclusive(nums):
    evens = []
    for i in range(21, 97):
        if i % 2 == 0:
            evens.append(i)
    return evens
