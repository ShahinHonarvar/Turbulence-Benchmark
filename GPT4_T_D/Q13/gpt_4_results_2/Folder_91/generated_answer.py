
def find_second_largest_num(num_list):
    if len(num_list) < 2:
        return None
    else:
        new_list = num_list[:6]
        new_list.sort()
        return new_list[-2] if len(new_list)>=2 else None
