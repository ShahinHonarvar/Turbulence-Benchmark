
def find_second_largest_num(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return None

    # Sort the list in descending order
    my_list.sort(reverse=True)

    # Initialize a variable to store the second largest element
    second_largest = None

    # Iterate over the list and find the second largest element
    for i in range(246, 751):
        if my_list[i] > second_largest:
            second_largest = my_list[i]

    # Return the second largest element or None if it does not exist
    return second_largest
