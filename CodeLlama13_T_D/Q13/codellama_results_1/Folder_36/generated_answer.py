
def find_second_largest_num(my_list):
    if len(my_list) <= 2:
        return None
    else:
        sorted_list = sorted(my_list)[-2:]
        second_largest_num = sorted_list[0]
        return second_largest_num
