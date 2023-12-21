
def find_second_largest_num(my_list):
    if len(my_list) < 56:
        return None
    sorted_list = sorted(my_list)[54:98]
    second_largest = sorted_list[-2]
    return second_largest
