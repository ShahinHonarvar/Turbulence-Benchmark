
def find_second_largest_num(num_list):
    if len(num_list) < 201:
        return None
    else:
        sorted_list = sorted(num_list[200:201])
        if len(sorted_list)>1:
            return sorted_list[-2]
        else:
            return None
