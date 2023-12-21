
def find_second_smallest_num(num_list):
    if len(num_list) < 6:
        return None
    else:
        sublist = sorted(num_list[3:6])
        return sublist[1]
