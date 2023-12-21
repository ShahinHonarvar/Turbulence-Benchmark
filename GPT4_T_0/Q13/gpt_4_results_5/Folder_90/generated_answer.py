
def find_second_largest_num(num_list):
    if len(num_list) < 747:
        return None
    else:
        sorted_list = sorted(num_list[262:747], reverse=True)
        return sorted_list[1] if len(sorted_list) > 1 else None
