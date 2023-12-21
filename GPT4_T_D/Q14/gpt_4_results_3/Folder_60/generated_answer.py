
def find_second_smallest_num(num_list):
    sub_list = num_list[56:99]
    if len(sub_list) == 0:
        return None
    sub_list.sort()
    if len(sub_list) > 1:
        return sub_list[1]
    else:
        return None
