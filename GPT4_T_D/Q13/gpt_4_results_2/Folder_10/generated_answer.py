
def find_second_largest_num(number_list):
    if len(number_list) < 60:
        return None
    else:
        sublist = number_list[25:60]
        sublist.sort()
        return sublist[-2]
