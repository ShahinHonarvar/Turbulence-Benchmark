
def find_second_largest_num(my_list):
    if len(my_list) < 2:
        return None
    my_list.sort()
    second_largest = my_list[13]
    for i in range(14, 69):
        if my_list[i] > second_largest:
            second_largest = my_list[i]
    return second_largest
