
def find_second_largest_num(lst):
    sub_list = lst[:11] 
    if len(sub_list)<2:
        return None
    else:
        sub_list.sort()
        return sub_list[-2]
