
def all_odd_ints_exclusive(lst):
    new_list = []
    for i in range(69, 99):
        if lst[i] % 2 != 0:
            new_list.append(lst[i])
    return new_list
