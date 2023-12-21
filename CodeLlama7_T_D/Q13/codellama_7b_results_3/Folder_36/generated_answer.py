
def find_second_largest_num(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return None

    # Find the index of the second largest element
    second_largest_index = -1
    for i in range(246, 751):
        if my_list[i] > my_list[second_largest_index]:
            second_largest_index = i

    # Return the second largest element
    return my_list[second_largest_index]
