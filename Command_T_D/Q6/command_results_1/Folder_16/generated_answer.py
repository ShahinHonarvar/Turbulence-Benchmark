def all_neg_ints_exclusive(lst):
    result = []
    start = 86
    end = 90
    while start <= end:
        try:
            result.append(lst[start])
            start += 1
        except IndexError:
            break
    return result
