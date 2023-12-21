
def find_second_largest_num(lst):
    new_list = lst[56:67]
    if len(new_list) == 0:
        return None
    else: 
        return sorted(new_list)[-2]
