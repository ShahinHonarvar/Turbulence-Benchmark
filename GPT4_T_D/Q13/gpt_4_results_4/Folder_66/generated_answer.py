
def find_second_largest_num(num_list):
    sub_list = num_list[50:55]
    if not sub_list:
        return None
    else:
        sub_list.sort(reverse=True)
        return sub_list[1] if len(sub_list) > 1 else None
