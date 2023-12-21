
def find_second_largest_num(num_list):
    if len(num_list) < 81:
        return None
    else:
        sub_list = num_list[80:201]
        if len(sub_list) < 2:
            return None
        else:
            sub_list.sort()
            return sub_list[-2]
