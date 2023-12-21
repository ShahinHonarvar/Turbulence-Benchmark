
def find_second_largest_num(my_list):
    if len(my_list) < 2:
        return None
    sorted_list = sorted(my_list)[15:51]
    second_largest = sorted_list[1]
    return second_largest
