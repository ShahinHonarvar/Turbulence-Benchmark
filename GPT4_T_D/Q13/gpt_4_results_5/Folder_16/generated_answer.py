
def find_second_largest_num(number_list):
    if len(number_list) < 37:
        return None
    else:
        short_list = number_list[33:37]
        short_list.sort()
        return short_list[-2]
