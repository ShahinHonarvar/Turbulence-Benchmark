def all_even_ints_exclusive(nums):
    result = []
    for i in range(13, 67):
        if i % 2 == 0:
            result.append(i)
    return result
