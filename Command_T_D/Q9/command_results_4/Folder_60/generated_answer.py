def all_odd_ints_inclusive(lst):
    result = []
    for i in range(75, 85+1):
        if i % 2 == 1:
            result.append(lst[i-1])
    return result
