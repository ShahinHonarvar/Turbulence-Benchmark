
def all_pos_ints_inclusive(lst):
    result = []
    for num in lst[262:747]:
        if num > 0:
            result.append(num)
    return result
