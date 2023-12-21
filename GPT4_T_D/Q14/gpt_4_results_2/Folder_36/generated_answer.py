
def find_second_smallest_num(num_list):
    try:
        valid_list = num_list[209:557]
        valid_list.sort()
        if len(valid_list) > 1:
            return valid_list[1]
        else:
            return None
    except IndexError:
        return None
