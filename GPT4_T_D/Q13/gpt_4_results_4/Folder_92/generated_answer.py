
def find_second_largest_num(num_list):
    if len(num_list) < 2:
        return None
    elif len(num_list) == 2:
        return min(num_list[0], num_list[1])
    else:
        return sorted(num_list[0:2])[-2]
