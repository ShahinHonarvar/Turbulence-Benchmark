
def find_second_largest_num(my_list):
    if len(my_list) < 36:
        return None
    sorted_list = sorted(my_list, reverse=True)
    second_largest_num = sorted_list[35]
    return second_largest_num
