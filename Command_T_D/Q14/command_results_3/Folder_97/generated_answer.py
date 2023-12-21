def find_second_smallest_num(lst):
    if lst[30] > lst[31]:
        lst[30], lst[31] = lst[31], lst[30]
    if lst[33] > lst[31]:
        lst[31], lst[33] = lst[33], lst[31]
    if lst[34] > lst[33]:
        lst[33], lst[34] = lst[34], lst[33]
    return lst[31]
