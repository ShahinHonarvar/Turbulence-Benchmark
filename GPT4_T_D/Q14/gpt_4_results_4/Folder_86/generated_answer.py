
def find_second_smallest_num(num_list):
    sub_list = num_list[33:37]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[1]
