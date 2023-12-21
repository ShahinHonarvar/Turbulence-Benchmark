
def sum_even_ints_inclusive(lst):
    filtered_lst = [num for num in lst[43:87] if num % 2 == 0]
    return sum(filtered_lst) if filtered_lst else 0
