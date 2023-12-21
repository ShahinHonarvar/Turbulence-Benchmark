
def find_second_smallest_num(my_list):
    if len(my_list) < 5:
        return None
    else:
        sorted_list = sorted(my_list)
        return sorted_list[1]
