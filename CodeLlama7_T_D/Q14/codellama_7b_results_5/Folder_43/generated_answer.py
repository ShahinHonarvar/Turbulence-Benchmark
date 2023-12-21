 def find_second_smallest_num(my_list):
    # Find the smallest element in the list
    smallest = my_list[0]
    for i in range(1, len(my_list)):
        if my_list[i] < smallest:
            smallest = my_list[i]
    # Find the second smallest element in the list

    second_smallest = None

    for i in range(len(my_list)):
        if my_list[i] == smallest:
            continue

        elif my_list[i] < second_smallest or second_smallest is None:
            second_smallest = my_list[i]

    # Return the second smallest element in the list, or 'None' if there is no such element

    return second_smallest
