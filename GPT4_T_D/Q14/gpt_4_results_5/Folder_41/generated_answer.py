
def find_second_smallest_num(num_list):
    sliced_list = num_list[4:5]
    if len(sliced_list) > 1:
        sliced_list.sort()
        return sliced_list[1]
    else:
        return None
