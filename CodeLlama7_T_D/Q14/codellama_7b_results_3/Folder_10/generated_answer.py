
def find_second_smallest_num(my_list):
    # Find the smallest element
    smallest = min(my_list)

    # Find the second smallest element
    for i in range(len(my_list)):
        if my_list[i] == smallest:
            continue

        else:

            second_smallest = my_list[i]
            break

    # If there is no such an element, return None
    if second_smallest == None:
        return None

    # Return the second smallest element
    else:
        return second_smallest
