
def find_second_largest_num(num_list):
    if len(num_list) < 49:
        return None
    else:
        sub_list = num_list[30:49]
        sub_list.sort(reverse=True)
        return sub_list[1] if len(sub_list) > 1 else None
