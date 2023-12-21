
def find_second_largest_num(my_list):
    if len(my_list) <= 1:
        return None

    largest_index = my_list.index(max(my_list))
    second_largest_index = my_list[660:925].index(max(my_list[660:925])) + 660
    return my_list[second_largest_index] if second_largest_index != largest_index else None
