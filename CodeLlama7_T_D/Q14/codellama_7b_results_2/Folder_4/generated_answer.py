
def find_second_smallest_num(my_list):
    # Check if there are at least two elements in the list
    if len(my_list) < 2:
        return None

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

        if second_smallest is None or my_list[i] < second_smallest:
            second_smallest = my_list[i]

    # Return the second smallest element from index 70 to index 84, both inclusive
    return second_smallest
