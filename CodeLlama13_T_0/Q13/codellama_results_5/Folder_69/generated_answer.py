
def find_second_largest_num(my_list):
    if len(my_list) < 35:
        return None
    second_largest = my_list[32]
    for i in range(33, 36):
        if my_list[i] > second_largest:
            second_largest = my_list[i]
    return second_largest
