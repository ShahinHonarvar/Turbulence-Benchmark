
def all_odd_ints_exclusive(lst):
    result = []
    for i in range(29, 53):
        if lst[i] % 2 != 0:
            result.append(lst[i])
    return result
