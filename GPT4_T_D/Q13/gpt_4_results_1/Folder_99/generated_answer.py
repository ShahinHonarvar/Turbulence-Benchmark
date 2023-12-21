
def find_second_largest_num(num_list):
    if len(num_list) >= 371:
        sliced_list = num_list[310:371]
        sliced_list.sort()
        return sliced_list[-2]
    else:
        return None
