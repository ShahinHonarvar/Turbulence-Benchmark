
def find_second_smallest_num(number_list):
    sub_list = number_list[25:88]
    if len(sub_list) == 0:
        return None
    elif len(sub_list) == 1:
        return None
    else:
        sub_list.sort()
        return sub_list[1]
