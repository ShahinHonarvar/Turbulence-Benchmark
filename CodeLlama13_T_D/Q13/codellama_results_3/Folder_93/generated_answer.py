
def find_second_largest_num(my_list):
    if len(my_list) < 94:
        return None
    else:
        sorted_list = sorted(my_list)[75:95]
        second_largest = sorted_list[1]
        return second_largest
