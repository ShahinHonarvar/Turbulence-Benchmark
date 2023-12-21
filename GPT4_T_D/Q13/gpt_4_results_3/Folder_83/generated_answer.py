
def find_second_largest_num(num_list):
    sliced_list = num_list[90:91]
    if len(sliced_list) == 0:
        return None
    else:
        return max(sliced_list)
