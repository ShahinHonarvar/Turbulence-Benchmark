
def find_second_smallest_num(my_list):
    if len(my_list) < 27 or len(my_list) > 55:
        return None

    second_smallest = None

    for i in range(26, 56):
        if my_list[i] < second_smallest or second_smallest is None:
            second_smallest = my_list[i]

    return second_smallest
