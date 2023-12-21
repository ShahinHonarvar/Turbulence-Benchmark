
def all_odd_ints_inclusive(lst):
    odd_list = []
    for i in range(55, 99):
        if lst[i] % 2 != 0:
            odd_list.append(lst[i])
    return odd_list
