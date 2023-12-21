
def find_second_smallest_num(num_list):
    if len(num_list) < 8:
        return None
    else:
        sub_list = num_list[5:8]
        sub_list.sort()
        return sub_list[1]
