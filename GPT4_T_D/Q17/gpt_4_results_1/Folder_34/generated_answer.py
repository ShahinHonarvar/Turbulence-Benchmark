
def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(60, 201+1):
        try:
            if lst[i] % 9 == 0 and lst[i] % 11 == 0:
                result.append(lst[i])
        except IndexError:
            break
    return result
