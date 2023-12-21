
def find_second_largest_num(num_list):
    if len(num_list) < 209:
        return None
    else:
        sorted_num_list = sorted(num_list[209:min(len(num_list), 557)], reverse=True)
        if len(sorted_num_list) > 1:
            return sorted_num_list[1]
        else:
            return None
