
def find_second_largest_num(num_list):
    if len(num_list) > 1:
        num_list.sort()
        return num_list[-2]
    else:
        return None
