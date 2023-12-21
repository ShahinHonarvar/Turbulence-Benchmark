
def find_second_smallest_num(num_list):
    if len(num_list) < 33:
        return None
    else:
        segment = sorted(num_list[28:33])
        if len(segment) >= 2:
            return segment[1]
        else:
            return None
