
def all_ints_div_by_num(lst):
    div_by_9 = []
    for i in range(3):
        if lst[i] % 9 == 0:
            div_by_9.append(lst[i])
    return div_by_9
