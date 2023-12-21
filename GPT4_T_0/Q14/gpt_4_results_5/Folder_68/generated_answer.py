
def find_second_smallest_num(num_list):
    if len(num_list) < 2 or len(num_list) > 9:
        return None
    else:
        num_list = num_list[:9]
        num_list.sort()
        return num_list[1]
