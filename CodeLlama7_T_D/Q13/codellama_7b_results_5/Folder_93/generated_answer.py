
def find_second_largest_num(my_list):
    if len(my_list) < 2:
        return None

    largest = my_list[75]

    for i in range(76, 94 + 1):

        if my_list[i] > largest:
            largest = my_list[i]

    for i in range(75, 94 + 1):

        if my_list[i] > largest and my_list[i] != my_list[75]:
            return my_list[i]

    return None
