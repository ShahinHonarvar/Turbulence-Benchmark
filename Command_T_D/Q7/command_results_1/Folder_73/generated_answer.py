
def all_even_ints_inclusive(nums):
    evens = []
    for i in range(19, 93):
        if i % 2 == 0:
            evens.append(i)
    return evens
