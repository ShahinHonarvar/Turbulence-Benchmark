
def find_second_largest_num(num_list):
    try:
        sublist = num_list[10:67]
        sublist.sort()
        return sublist[-2]
    except IndexError:
        return None
