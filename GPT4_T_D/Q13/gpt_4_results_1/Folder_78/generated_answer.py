
def find_second_largest_num(num_list):
    if len(num_list) < 52:
        return None
    else:
        sub_list = sorted(num_list[43:52], reverse=True)
        if len(sub_list) >= 2:
            return sub_list[1]
        else:
            return None
