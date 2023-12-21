
def find_second_largest_num(num_list):
    if len(num_list[90:91]) < 2:
        return None
    else:
        sorted_list = sorted(num_list[90:91])
        return sorted_list[-2]
