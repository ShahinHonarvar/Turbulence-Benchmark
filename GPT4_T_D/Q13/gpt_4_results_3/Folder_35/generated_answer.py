
def find_second_largest_num(num_list):
    if len(num_list) < 49:
        return None
    else:
        return sorted(num_list[30:49], reverse=True)[1]
