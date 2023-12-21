
def find_second_largest_num(num_list):
    if len(num_list) < 11:
        return None
    else:
        sorted_list = sorted(num_list[10:67], reverse=True)
        if len(sorted_list) < 2:
            return None
        else:
            return sorted_list[1]
