
def find_second_smallest_num(num_list):
    if len(num_list) < 96 or len(num_list[74:96]) < 2:
        return None
    else:
        return sorted(num_list[74:96])[1]
