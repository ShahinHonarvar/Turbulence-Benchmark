
def find_second_largest_num(my_list):
    if len(my_list) < 2:
        return None
    my_list.sort()
    largest = my_list[-1]
    second_largest = my_list[-2]
    for i in range(30,88):
        if my_list[i] == largest:
            continue
        elif my_list[i] > second_largest:
            second_largest = my_list[i]
    return second_largest
