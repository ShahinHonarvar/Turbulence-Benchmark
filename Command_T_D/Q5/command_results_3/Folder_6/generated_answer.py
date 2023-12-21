def all_neg_ints_inclusive(lst):
    result = []
    start = 10
    end = 66
    while start <= end:
        try:
            result.append(lst[start])
            start += 1
        except:
            break
    return result
