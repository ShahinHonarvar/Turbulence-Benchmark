
def find_second_largest_num(num_list):
    if len(num_list) < 775:
        return None
    else:
        sorted_list = sorted(num_list[667:775])
        return sorted_list[-2]
