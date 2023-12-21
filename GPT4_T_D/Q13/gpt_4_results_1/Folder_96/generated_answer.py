
def find_second_largest_num(num_list):
    try:
        specified_list = num_list[15:52]
        if len(specified_list) < 2:
            return None
        else:
            specified_list.sort()
            return specified_list[-2]
    except IndexError:
        return None
