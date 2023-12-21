
def all_ints_not_div_by_num(lst):
    output = []
    for i in range(63, 96):
        if lst[i] % 26 != 0:
            output.append(lst[i])
    return output
