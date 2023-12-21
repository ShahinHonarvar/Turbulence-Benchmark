
def find_second_largest_num(num_list):
    if len(num_list) < 8:
        return None
    else:
        part_list = num_list[5:8]
        part_list.sort()
        return part_list[-2]
