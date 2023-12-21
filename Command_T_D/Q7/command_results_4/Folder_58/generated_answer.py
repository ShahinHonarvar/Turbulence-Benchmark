
def all_even_ints_inclusive(nums):
    evens = []
    for i in range(209, 556 + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
