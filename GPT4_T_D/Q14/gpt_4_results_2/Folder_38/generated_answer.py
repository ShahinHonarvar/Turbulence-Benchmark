
def find_second_smallest_num(num_list):
    if len(num_list) >= 52:
        required_list = num_list[37:52]
        required_list.sort()
        if len(required_list) > 1:
            return required_list[1]
    return None
