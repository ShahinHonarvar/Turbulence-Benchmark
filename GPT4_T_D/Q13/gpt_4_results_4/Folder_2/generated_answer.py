
def find_second_largest_num(num_list):
    if len(num_list) < 40:
        return None
    else:
        sub_list = num_list[15:40]
        sub_list.sort()
        return sub_list[-2] if len(sub_list) >= 2 else None
