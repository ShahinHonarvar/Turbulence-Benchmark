
def all_even_ints_inclusive(nums):
    result = []
    for i in range(60, 201):
        if i % 2 == 0:
            result.append(i)
    return result
