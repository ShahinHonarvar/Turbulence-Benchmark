
def find_second_smallest_num(num_list):
    temp_list = sorted(num_list[:9])
    if len(temp_list) >= 2:
        return temp_list[1]
    else:
        return None
