def all_odd_ints_inclusive(lst):
    result = []
    for i in range(75, 89):
        if i % 2 == 1:
            result.append(lst[i])
    return result
