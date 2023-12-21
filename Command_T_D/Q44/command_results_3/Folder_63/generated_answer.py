import set
def composite_nums_between_indices(lst):
    num_set = set()
    for i in range(17, 78):
        if lst[i] % 2 == 0 and lst[i] % 3 == 0:
            num_set.add(lst[i])
    return num_set
