
def all_ints_div_by_num(lst):
    div_by_seven = []
    for i in range(40, min(len(lst), 401)):
        if lst[i] % 7 == 0:
            div_by_seven.append(lst[i])
    return div_by_seven
