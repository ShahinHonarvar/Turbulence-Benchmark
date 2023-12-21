
def find_second_smallest_num(num_list):
    if len(num_list)<=4:
        return None
    sorted_list = sorted(num_list[:4])
    if len(sorted_list)>1:
        return sorted_list[1]
    else:
        return None
