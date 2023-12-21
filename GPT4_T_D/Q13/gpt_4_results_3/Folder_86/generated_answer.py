
def find_second_largest_num(num_list):
    sublist = num_list[31:35]
    if len(sublist) < 2:
        return None
    else:
        return sorted(sublist, reverse=True)[1]
