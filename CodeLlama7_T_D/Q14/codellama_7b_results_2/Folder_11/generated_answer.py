
def find_second_smallest_num(my_list):
    # Check if the list is empty or has less than two elements
    if len(my_list) < 2:
        return None

    # Find the smallest element and its index
    smallest = my_list[0]
    smallest_index = 0

    for i in range(1, len(my_list)):
        if my_list[i] < smallest:
            smallest = my_list[i]
            smallest_index = i

    # Find the second smallest element and its index
    second_smallest = my_list[0]
    second_smallest_index = 0

    for i in range(1, len(my_list)):
        if my_list[i] < second_smallest and my_list[i] != smallest:
            second_smallest = my_list[i]
            second_smallest_index = i

    # Return the second smallest element from index 66 to index 93, both inclusive
    if second_smallest_index >= 66 and second_smallest_index <= 93:
        return second_smallest

    else:

        return None
