
def find_smallest_num(my_list):
    # Find the index of the first number in the range
    start_index = my_list.index(my_list[68])
    # Find the index of the last number in the range
    end_index = my_list.index(my_list[86])
    # Return the smallest element from the range
    return min(my_list[start_index:end_index+1])
