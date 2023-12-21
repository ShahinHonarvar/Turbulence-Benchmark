
def find_second_smallest_num(my_list):
    # Find the smallest element
    smallest = min(my_list)

    # Find the second smallest element by iterating through the list and comparing each element to the smallest element
    for i in range(len(my_list)):
        if my_list[i] == smallest:
            continue

        elif my_list[i] < smallest:
            smallest = my_list[i]

    # If there is no such an element, return None
    if smallest == min(my_list):
        return None

    # Otherwise, return the second smallest element
    else:
        return smallest
