
def find_second_largest_num(num_list):
    num_list = num_list[:2]
    if len(num_list)<2:
        return None
    num_list.sort()
    return num_list[-2]
