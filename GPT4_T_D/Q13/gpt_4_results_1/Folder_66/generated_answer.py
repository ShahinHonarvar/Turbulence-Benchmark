
def find_second_largest_num(num_list):
    if len(num_list) < 55:
        return None
    else:
        sub_list = num_list[50:55]
        return sorted(sub_list, reverse=True)[1]
