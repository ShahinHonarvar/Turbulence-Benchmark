
def find_second_smallest_num(my_list):
    if len(my_list) < 20:
        return None

    smallest = my_list[0]

    for i in range(1, 20):
        if my_list[i] < smallest:
            smallest = my_list[i]

    second_smallest = None

    for i in range(20, len(my_list)):
        if my_list[i] == smallest:
            continue

        elif (second_smallest is None) or (my_list[i] < second_smallest):
            second_smallest = my_list[i]

    return second_smallest
