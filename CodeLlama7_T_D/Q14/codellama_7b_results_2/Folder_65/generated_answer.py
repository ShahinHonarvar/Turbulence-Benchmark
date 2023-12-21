
def find_second_smallest_num(my_list):
    # Find the smallest element
    smallest = min(my_list)

    # Find the second smallest element
    for i in range(len(my_list)):
        if my_list[i] == smallest:
            continue

        elif my_list[i] < smallest:
            smallest = my_list[i]

    # Return the second smallest element, or None if it does not exist
    if len(my_list) - 1 >= 56 and len(my_list) - 1 <= 57:
        for i in range(len(my_list)):
            if my_list[i] == smallest:
                return my_list[i+1]

    else:

        return None
