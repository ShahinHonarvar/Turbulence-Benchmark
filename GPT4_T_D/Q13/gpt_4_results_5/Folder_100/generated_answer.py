
def find_second_largest_num(num_list):
    if len(num_list) < 69:
        return None
    else:
        sublist = num_list[42:69]
        sublist.sort()
        return sublist[-2]
