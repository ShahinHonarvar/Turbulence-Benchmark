
def sum_even_ints_inclusive(lst):
    sliced_lst = lst[70:201]
    even_sum = sum(i for i in sliced_lst if i % 2 == 0)
    return even_sum
