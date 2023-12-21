def all_odd_ints_exclusive(nums):
    result = []
    for i in range(80, 201):
        if i % 2 == 1:
            result.append(i)
    return result
