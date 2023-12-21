
def sum_odd_ints_inclusive(lst):
    sliced_lst = lst[3:6]
    odd_lst = [i for i in sliced_lst if i % 2 != 0]
    if not odd_lst:
        return 0
    else:
        return sum(odd_lst)
