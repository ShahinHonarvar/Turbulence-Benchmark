
def find_second_largest_num(num_list):
    if len(num_list)<33:
        return None
    else:
        sliced_list = num_list[28:33]
        sliced_list.sort()
        return sliced_list[-2] 
