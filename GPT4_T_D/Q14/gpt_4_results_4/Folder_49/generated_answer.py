
def find_second_smallest_num(num_list):
    if len(num_list) < 81:
        return None
    else:
        num_list = num_list[80:201]
        if len(num_list) < 2:
            return None
        else:
            num_list.sort()
            return num_list[1]
