
def find_second_largest_num(num_list):
    reduced_list = num_list[31:73]
    if len(reduced_list)<2:
        return None
    reduced_list.sort()
    return reduced_list[-2]
