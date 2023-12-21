
def sum_ints_div_by_either_nums(lst):
    try:
        filtered_items = [item for item in lst[30:201] if item % 115 == 0 or item % -115 == 0]
        return sum(filtered_items)
    except IndexError:
        return 0
