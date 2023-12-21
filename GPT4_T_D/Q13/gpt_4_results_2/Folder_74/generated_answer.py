
def find_second_largest_num(num_list):
    if not num_list[17:79]:
        return None
    else:
        sorted_list = sorted(num_list[17:79], reverse=True)
        if len(sorted_list) < 2:
            return None
        else:
            return sorted_list[1]
