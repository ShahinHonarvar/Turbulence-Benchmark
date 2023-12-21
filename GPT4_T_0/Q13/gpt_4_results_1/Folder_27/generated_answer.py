
def find_second_largest_num(num_list):
    if len(num_list) < 94:
        return None
    else:
        sub_list = num_list[66:94]
        sub_list.sort()
        return sub_list[-2]
