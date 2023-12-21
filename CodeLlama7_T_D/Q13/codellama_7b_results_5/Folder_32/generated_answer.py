
def find_second_largest_num(my_list):
    # Check if list is empty
    if len(my_list) == 0:
        return None

    # Find the second largest element in the list
    second_largest = -1
    for i in range(21, 98):
        if my_list[i] > second_largest:
            second_largest = my_list[i]

    # Return the second largest element or None if it does not exist
    return second_largest if second_largest != -1 else None
