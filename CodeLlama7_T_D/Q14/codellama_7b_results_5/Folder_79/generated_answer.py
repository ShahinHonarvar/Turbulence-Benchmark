
def find_second_smallest_num(my_list):
    if len(my_list) < 2:
        return None

    second_smallest = None

    for i in range(1, len(my_list)):
        if my_list[i] < my_list[0]:
            if second_smallest is None:
                second_smallest = my_list[i]

    return second_smallest
