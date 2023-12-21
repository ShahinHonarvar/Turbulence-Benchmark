
def find_second_largest_num(lst):
    num_list = sorted(lst[28:39], reverse=True)
    if len(num_list) < 2:
        return None
    else:
        return num_list[1]
