
def sum_ints_div_by_either_nums(lst):
    sliced_list = lst[86:91]
    total = sum([num for num in sliced_list if num % -71 == 0 or num % -67 == 0])
    return total
