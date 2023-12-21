
def sum_ints_div_by_either_nums(lst):
    selected_ints = lst[61:89]
    return sum(val for val in selected_ints if val%31==0 or val%11==0)
