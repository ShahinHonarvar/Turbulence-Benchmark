def sum_in_range(lst):
    result = sum(lst[i] for i in range(len(lst)) if 72 <= lst[i] <= 93)
    return result
