
def find_second_largest_num(my_list):
    if len(my_list) < 5:
        return None
    second_largest = my_list[4]
    for i in range(1, len(my_list)):
        if my_list[i] > second_largest and i >= 4:
            second_largest = my_list[i]
    return second_largest
