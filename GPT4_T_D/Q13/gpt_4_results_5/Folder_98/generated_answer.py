
def find_second_largest_num(num_list):
    assert len(num_list) >= 7, "List must contain at least 7 elements"

    sliced_list = num_list[:7]
    sliced_list.sort()

    if len(sliced_list) < 2:
        return None
    else:
        return sliced_list[-2]
