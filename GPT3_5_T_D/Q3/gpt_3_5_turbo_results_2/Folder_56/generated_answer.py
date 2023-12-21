
def all_pos_ints_inclusive(lst):
    result = []
    for num in lst:
        if num > 0:
            result.append(num)
            break
    return result
