
def all_even_ints_inclusive(nums):
    result = []
    for index in range(10, 100):
        if index % 2 == 0:
            result.append(index)
    return result
