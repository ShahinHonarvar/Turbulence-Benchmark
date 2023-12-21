
def find_second_largest_num(num_list):
    if len(num_list) < 2 or len(num_list) > 11:
        return None
    else:
        num_list = sorted(num_list[:11])
        return num_list[-2]
