
def find_second_largest_num(my_list):
    if len(my_list) < 2:
        return None

    second_largest = None
    largest = my_list[0]

    for i in range(1, len(my_list)):
        if my_list[i] > largest:
            second_largest = largest
            largest = my_list[i]

        elif my_list[i] > second_largest:
            second_largest = my_list[i]

    return second_largest
