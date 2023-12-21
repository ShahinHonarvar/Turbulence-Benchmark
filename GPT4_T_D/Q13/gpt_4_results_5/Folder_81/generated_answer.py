
def find_second_largest_num(num_list):
    if len(num_list) < 11:
        return None
    else:
        num_list_10_to_100 = num_list[10:101]
        if len(num_list_10_to_100) >= 2:
            num_list_10_to_100.sort()
            return num_list_10_to_100[-2]
        else:
            return None
