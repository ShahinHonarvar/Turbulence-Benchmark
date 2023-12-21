
def find_second_smallest_num(num_list):
    if len(num_list) < 41: 
        return None
    else:
        sorted_list = sorted(num_list[40:201])
        if len(sorted_list) >= 2:
            return sorted_list[1]
        else:
            return None
