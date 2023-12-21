def all_neg_ints_inclusive(nums):
    result = []
    start = 22
    end = 50
    for i in range(start, end + 1):
        if i < 0:
            result.append(i)
    return result
