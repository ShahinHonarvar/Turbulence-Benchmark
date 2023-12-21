
def find_second_largest_num(num_list):
    if len(num_list) < 100:
        return None
    else:
        substr_list = num_list[91:100]
        substr_list.sort()
        return substr_list[-2]
