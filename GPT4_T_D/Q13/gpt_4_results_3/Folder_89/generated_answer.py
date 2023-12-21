
def find_second_largest_num(num_list):
    if len(num_list)<83:
        return None
    else:
        sublist = num_list[56:83]
        sublist.sort()
        return sublist[-2]
