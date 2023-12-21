
def find_second_largest_num(num_list):
    if len(num_list) < 2:
        return None
    else:
        num_list = num_list[:2]
        num_list.sort()
        return num_list[0]
