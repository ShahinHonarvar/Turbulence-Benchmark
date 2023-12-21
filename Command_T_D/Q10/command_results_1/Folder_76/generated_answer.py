def all_odd_ints_exclusive(nums):
    result = []
    for i in range(361, 643):
        if i % 2 == 1:
            result.append(i)
    return result
