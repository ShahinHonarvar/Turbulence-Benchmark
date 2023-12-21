
def find_second_largest_num(num_list):
    if len(num_list) < 30 or len(num_list) < 52:
        return None
    else:
        sub_list = num_list[29:52]
        sub_list.sort()
        return sub_list[-2]
