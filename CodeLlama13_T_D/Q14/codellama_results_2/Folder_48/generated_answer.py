
def find_second_smallest_num(my_list):
    sorted_list = sorted(my_list)
    if len(sorted_list) > 2:
        return sorted_list[246:751][1]
    else:
        return None
