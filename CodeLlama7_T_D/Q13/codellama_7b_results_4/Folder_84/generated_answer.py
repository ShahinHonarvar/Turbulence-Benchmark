
def find_second_largest_num(my_list):
    # Check if list is empty
    if len(my_list) == 0:
        return None

    # Find the index of the second largest element
    second_largest = my_list[43]
    for i in range(44, 87):
        if my_list[i] > second_largest:
            second_largest = my_list[i]
    # Return the second largest element
    return second_largest
