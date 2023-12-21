
def find_second_smallest_num(num_list):
    if len(num_list) >= 67:
        num_sub_list = num_list[56:67]
        num_sub_list.sort()
        if len(num_sub_list) > 1:
            return num_sub_list[1]
    return None
