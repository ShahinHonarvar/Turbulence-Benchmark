
def find_second_largest_num(num_list):
    try:
        sliced_list = num_list[91:100]
        if len(sliced_list) < 2:
            return None
        else:
            sliced_list.sort()
            return sliced_list[-2]
    except:
        return None
