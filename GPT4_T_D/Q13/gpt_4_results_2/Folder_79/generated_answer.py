
def find_second_largest_num(num_list):
    if len(num_list) < 5:
        return None
    else:
        sliced_list = num_list[4:5]
        if len(sliced_list) < 2:
            return None
        else:
            sliced_list.sort()
            return sliced_list[-2]
