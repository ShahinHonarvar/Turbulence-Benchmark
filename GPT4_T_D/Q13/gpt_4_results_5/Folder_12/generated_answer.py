
def find_second_largest_num(number_list):
    if len(number_list) < 15:
        return None
    sub_list = number_list[14:65]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[-2]
