
def find_second_smallest_num(num_list):
    sliced_list = num_list[62:79]
    if len(sliced_list) > 1:
        sorted_list = sorted(sliced_list)
        return sorted_list[1]
    else:
        return None
