
def find_second_largest_num(num_list):
    if len(num_list) < 774:
        return None
    else:
        sub_list = num_list[667:775]
        sub_list.sort()
        return sub_list[-2]
