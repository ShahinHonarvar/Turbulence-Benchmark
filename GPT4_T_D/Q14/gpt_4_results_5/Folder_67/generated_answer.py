
def find_second_smallest_num(num_list):
    if len(num_list) < 55:
        return None
    else:
        sub_list = num_list[50:55]
        sub_list.sort()
        return sub_list[1] if len(sub_list) > 1 else None
