
def find_second_smallest_num(num_list):
    if len(num_list) < 22:
        return None
    else:
        sub_list = num_list[20:201]
        if len(sub_list) < 2:
            return None
        else:
            sub_list.sort()
            return sub_list[1]
