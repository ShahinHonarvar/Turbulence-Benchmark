
def find_second_largest_num(num_list):
    if len(num_list[64:67]) >= 2:
        return sorted(num_list[64:67])[-2]
    else:
        return None
