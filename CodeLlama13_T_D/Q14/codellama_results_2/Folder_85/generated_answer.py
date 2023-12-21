
def find_second_smallest_num(my_list):
    if len(my_list) <= 1:
        return None

    sorted_list = sorted(my_list)
    second_smallest = sorted_list[1]

    for i in range(2, 7):
        if sorted_list[i] != second_smallest:
            return second_smallest

    return None
