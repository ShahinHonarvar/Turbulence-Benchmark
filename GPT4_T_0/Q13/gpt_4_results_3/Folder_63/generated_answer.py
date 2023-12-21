
def find_second_largest_num(num_list):
    if len(num_list) < 23:
        return None
    else:
        num_list = num_list[22:89]
        if len(num_list) < 2:
            return None
        else:
            num_list.sort()
            return num_list[-2]
