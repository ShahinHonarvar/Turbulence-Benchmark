
def find_second_smallest_num(num_list):
    if len(num_list) < 605:
        return None
    else:
        sort_list = sorted(num_list[533:606])
        if len(sort_list) < 2:
            return None
        else:
            return sort_list[1]
