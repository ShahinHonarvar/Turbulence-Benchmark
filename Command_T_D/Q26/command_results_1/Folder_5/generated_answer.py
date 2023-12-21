def sum_in_range(lst):
    result = 0
    for item in lst:
        if item >= 6 and item <= 8:
            result += item
    return result
