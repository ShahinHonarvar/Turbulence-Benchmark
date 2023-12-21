
def find_second_largest_num(num_list):
    if len(num_list[25:88]) > 1:
        num_list = sorted(num_list[25:88])
        return num_list[-2]
    else:
        return None
