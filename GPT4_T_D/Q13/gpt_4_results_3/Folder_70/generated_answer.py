
def find_second_largest_num(num_list):
    if len(num_list) < 33 or len(num_list[28:33]) < 2:
        return None
    else:
        return sorted(num_list[28:33], reverse=True)[1]
