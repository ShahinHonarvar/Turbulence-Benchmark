
def find_second_largest_num(num_list):
    if len(num_list) >= 64:
        num_list = num_list[62:64]
        num_list.sort()
        return num_list[-2]
    else:
        return None
