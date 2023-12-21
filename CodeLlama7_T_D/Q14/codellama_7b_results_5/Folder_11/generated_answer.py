
def find_second_smallest_num(my_list):
    # Check if there is a second smallest element in the list
    if len(my_list) < 2:
        return None

    # Sort the list in ascending order
    my_list.sort()

    # Get the index of the second smallest element
    second_smallest_index = -1
    for i in range(66, 94):
        if my_list[i] != my_list[i-1]:
            second_smallest_index = i
            break

    # Return the second smallest element or 'None' if there is no such element
    if second_smallest_index != -1:
        return my_list[second_smallest_index]

    else:

        return None
