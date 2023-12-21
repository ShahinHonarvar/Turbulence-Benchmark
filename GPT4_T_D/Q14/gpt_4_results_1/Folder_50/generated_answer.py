
def find_second_smallest_num(num_list):
    try:
        subset_list = num_list[42:69]
        if len(subset_list) < 2:
            return None
        else:
            return sorted(subset_list)[1]
    except IndexError:
        return None
