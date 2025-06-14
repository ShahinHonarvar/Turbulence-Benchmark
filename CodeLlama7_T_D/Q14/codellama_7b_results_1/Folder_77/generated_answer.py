
def find_second_smallest_num(my_list):
    # Find the smallest element in the list
    smallest = min(my_list)

    # Find the second smallest element in the list
    for i in range(len(my_list)):
        if my_list[i] == smallest:
            continue

        elif my_list[i] < smallest:
            smallest = my_list[i]

    # Return the second smallest element, or None if it doesn't exist
    if len(my_list) > 1 and smallest != my_list[-1]:
        return smallest

    else:

        return None
