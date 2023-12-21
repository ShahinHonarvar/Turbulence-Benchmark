
def sum_odd_ints_inclusive(lst):
    selected_lst = lst[70:85]
    odd_sum = sum(i for i in selected_lst if i%2!=0)
    return odd_sum
