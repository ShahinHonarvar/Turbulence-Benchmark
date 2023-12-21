
def find_second_largest_num(my_list):
    if len(my_list) < 8:
        return None
    second_largest = my_list[5]
    for i in range(6, 9):
        if my_list[i] > second_largest:
            second_largest = my_list[i]
    return second_largest
