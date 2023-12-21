
def find_second_smallest_num(num_list):
    if len(num_list) < 98:
        return None
    else:
        new_list = sorted(num_list[55:99])
        if len(new_list) < 2:
            return None
        else:
            return new_list[1]
