
def find_second_largest_num(my_list):
    largest = None
    second_largest = None
    for i in range(29, 80):
        if my_list[i] > largest:
            second_largest = largest
            largest = my_list[i]
        elif my_list[i] > second_largest:
            second_largest = my_list[i]
    return second_largest
