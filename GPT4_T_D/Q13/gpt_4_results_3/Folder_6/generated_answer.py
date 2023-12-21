
def find_second_largest_num(num_list):
    if len(num_list) < 11:
        return None
    else:
        num_list = num_list[10:min(len(num_list), 67)]
        num_list.sort()
        if len(num_list) > 1:
            return num_list[-2]
        else:
            return None
