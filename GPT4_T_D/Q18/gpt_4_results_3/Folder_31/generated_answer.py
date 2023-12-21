
def sum_ints_div_by_either_nums(lst):
    selected_elements = lst[56:89]
    total = sum([num for num in selected_elements if num % -59 == 0 or num % -79 == 0])
    return total
