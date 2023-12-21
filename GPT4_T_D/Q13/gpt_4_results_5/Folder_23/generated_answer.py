
def find_second_largest_num(n_list):
    if len(n_list) < 72:
        return None
    else:
        sub_list = sorted(n_list[52:72])
        if len(sub_list) < 2:
            return None
        else:
            return sub_list[-2]
