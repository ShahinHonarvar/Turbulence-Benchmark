
def find_second_smallest_num(my_list):
    if len(my_list) < 29 or len(my_list) > 79:
        return None

    second_smallest = None

    for i in range(29, 80):
        if my_list[i] < second_smallest or second_smallest is None:
            second_smallest = my_list[i]

    return second_smallest
