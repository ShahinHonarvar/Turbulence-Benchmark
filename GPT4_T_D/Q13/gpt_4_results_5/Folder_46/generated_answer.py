
def find_second_largest_num(num_list):
    index_slice = num_list[30:88]
    if len(index_slice) < 2:
        return None
    else:
        index_slice.sort()
        return index_slice[-2]
