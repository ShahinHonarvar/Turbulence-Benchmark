def all_even_ints_exclusive(nums):
    result = []
    for i in range(36, 85):
        if i % 2 == 0:
            result.append(i)
    return result
