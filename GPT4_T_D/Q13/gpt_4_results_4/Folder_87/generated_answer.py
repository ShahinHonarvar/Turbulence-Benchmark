
def find_second_largest_num(num_list):
    sub_list = num_list[36:47]
    if len(sub_list) < 2:
        return None
    else:
        sub_list.sort()
        return sub_list[-2]
