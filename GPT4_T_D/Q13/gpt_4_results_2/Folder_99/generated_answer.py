
def find_second_largest_num(num_list):
    slice_list = num_list[310:371] 
    if len(slice_list) < 2:
        return None
    slice_list.sort() 
    return slice_list[-2]
