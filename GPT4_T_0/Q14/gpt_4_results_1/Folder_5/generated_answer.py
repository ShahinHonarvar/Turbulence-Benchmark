
def find_second_smallest_num(num_list):
    if len(num_list) < 6:
        return None
    else:
        sub_list = num_list[3:6]
        sub_list.sort()
        return sub_list[1]
