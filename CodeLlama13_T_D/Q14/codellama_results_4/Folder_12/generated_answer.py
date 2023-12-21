
def find_second_smallest_num(my_list):
    if len(my_list) < 73:
        return None
    else:
        sorted_list = sorted(my_list[31:73])
        return sorted_list[1]
