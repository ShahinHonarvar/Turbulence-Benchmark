
def find_second_largest_num(num_list):
    try:
        slice_list = num_list[28:33]
        slice_list.sort()
        return slice_list[-2]
    except IndexError:
        return None
    except:
        return None
