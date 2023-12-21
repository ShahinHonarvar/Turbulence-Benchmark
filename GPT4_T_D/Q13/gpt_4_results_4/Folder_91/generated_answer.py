
def find_second_largest_num(num_list):
    if len(num_list) < 2 or num_list == None:
        return None
    num_list = num_list[:6]
    num_list.sort()
    return num_list[-2]
