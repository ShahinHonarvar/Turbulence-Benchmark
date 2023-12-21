
def find_second_largest_num(num_list):
    if len(num_list) < 31:
        return None
    else:
        num_list = num_list[30:201] if len(num_list) > 200 else num_list[30:]
        if len(num_list) == 0:
            return None
        else:
            num_list.sort()
            return num_list[-2] if len(num_list) > 1 else None
