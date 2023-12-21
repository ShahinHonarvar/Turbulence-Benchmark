
def find_second_largest_num(lst):
    sub_list = lst[23:24]
    if len(sub_list)<2:
        return None
    else:
        return sorted(sub_list)[-2]
