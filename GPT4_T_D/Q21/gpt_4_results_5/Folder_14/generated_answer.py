
def all_ints_div_by_num(lst):
    if len(lst) < 9:
        return []
    else:
        temp_lst = [lst[8]]
        return [i for i in temp_lst if i % 8 == 0]
