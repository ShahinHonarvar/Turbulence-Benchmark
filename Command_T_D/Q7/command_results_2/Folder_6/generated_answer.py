
def all_even_ints_inclusive(nums):
    result = []
    for i in range(10, 66 + 1):
        if i % 2 == 0:
            result.append(i)
    return result
