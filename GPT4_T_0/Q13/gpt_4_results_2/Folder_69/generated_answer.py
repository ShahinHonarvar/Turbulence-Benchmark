
def find_second_largest_num(num_list):
    if len(num_list) < 36:
        return None
    else:
        sub_list = num_list[32:36]
        sub_list.sort()
        return sub_list[-2]
