def all_ints_exclusive(lst):
    result = []
    for i in range(2, len(lst) - 1):
        result += lst[i:i + 2]
    return result
