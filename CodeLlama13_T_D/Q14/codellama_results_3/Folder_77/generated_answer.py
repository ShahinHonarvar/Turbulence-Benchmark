
def find_second_smallest_num(my_list):
    if len(my_list) < 639 or len(my_list) > 975:
        return None
    else:
        return sorted(my_list[639:976])[1]
