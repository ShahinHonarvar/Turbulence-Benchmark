
def find_second_largest_num(num_list):
    try:
        new_list = num_list[29:52]
        new_list.sort()
        return new_list[-2]
    except:
        return None
