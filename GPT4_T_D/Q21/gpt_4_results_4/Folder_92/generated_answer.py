
def all_ints_div_by_num(lst):
    result = []
    for i in range(len(lst)):
        if i <= 0 and lst[i] % 1 == 0:
            result.append(lst[i])
    return result
