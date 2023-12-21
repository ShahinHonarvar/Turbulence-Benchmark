
def find_second_smallest_num(number_list):
    if len(number_list) < 24:
        return None
    else:
        sorted_list = sorted(number_list[22:64])
        if len(sorted_list) < 2:
            return None
        else:
            return sorted_list[1]
