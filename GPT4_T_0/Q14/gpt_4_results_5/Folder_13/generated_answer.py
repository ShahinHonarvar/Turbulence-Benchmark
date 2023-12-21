
def find_second_smallest_num(num_list):
    if len(num_list) < 33:
        return None
    else:
        sub_list = num_list[28:33]
        sub_list.sort()
        return sub_list[1]
