
def all_ints_div_by_num(lst):
    div_ints = []
    for i in range(11, 83):
        if lst[i] % -47 == 0:
            div_ints.append(lst[i])
    return div_ints
