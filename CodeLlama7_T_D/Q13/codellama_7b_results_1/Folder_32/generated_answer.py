
def find_second_largest_num(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return None

    # Sort the list in descending order
    my_list.sort(reverse=True)

    # Initialize variables to keep track of the second largest element and its index
    second_largest = None
    second_largest_index = None

    # Iterate through the list starting from index 21 to index 97
    for i in range(21, 98):
        # If the current element is greater than the second largest element, update the second largest element and its index
        if my_list[i] > second_largest:
            second_largest = my_list[i]
            second_largest_index = i

    # Return the second largest element from index 21 to index 97, both inclusive
    return second_largest
