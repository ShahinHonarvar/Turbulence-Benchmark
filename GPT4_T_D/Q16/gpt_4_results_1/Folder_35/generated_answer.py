
def sum_even_ints_inclusive(lst):
    slice_lst = lst[30:49]
    sum_list = [num for num in slice_lst if num % 2 == 0]
    return sum(sum_list) if sum_list else 0
