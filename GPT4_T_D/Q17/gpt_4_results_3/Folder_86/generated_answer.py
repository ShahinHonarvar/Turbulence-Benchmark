
def all_ints_div_by_both_two_nums(lst):
    div_ints = []
    for i in range(54, 80):
        if lst[i] % 54 == 0 and lst[i] % 28 == 0:
            div_ints.append(lst[i])
    return div_ints
