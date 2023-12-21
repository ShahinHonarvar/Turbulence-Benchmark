
def sum_odd_ints_inclusive(lst):
    filtered_list = [x for x in lst[37:77] if x%2 != 0]
    if not filtered_list:
        return 0
    else:
        return sum(filtered_list)
