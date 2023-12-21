
def find_second_largest_num(my_list):
    # Check if list is empty
    if len(my_list) == 0:
        return None

    # Find the index of the largest element
    largest_index = my_list.index(max(my_list))

    # Find the index of the second largest element
    second_largest_index = -1
    for i in range(len(my_list)):
        if i != largest_index and my_list[i] > my_list[second_largest_index]:
            second_largest_index = i

    # Return the second largest element, or None if it doesn't exist
    if second_largest_index == -1:
        return None

    else:

        return my_list[second_largest_index]
