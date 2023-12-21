
def find_second_smallest_num(my_list):
    if len(my_list) < 2:
        return None

    second_smallest = float('inf')

    for i in range(34, 56):
        if my_list[i] < second_smallest:
            second_smallest = my_list[i]

    return second_smallest
