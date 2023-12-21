
def find_second_largest_num(num_list):
    sublist = num_list[40:81]
    if not sublist:
        return None
    sublist.sort()
    return sublist[-2] if len(sublist) > 1 else None
