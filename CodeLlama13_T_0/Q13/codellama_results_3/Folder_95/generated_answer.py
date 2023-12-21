
def find_second_largest_num(my_list):
    if len(my_list) < 86:
        return None
    second_largest = my_list[82]
    for i in range(83, 87):
        if my_list[i] > second_largest:
            second_largest = my_list[i]
    return second_largest
