
def find_second_largest_num(num_list):
    sublist = num_list[8:10]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]
