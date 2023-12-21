
def find_second_largest_num(my_list):
    # Check if the list is empty or None
    if not my_list:
        return None

    # Sort the list in descending order
    my_list.sort(reverse=True)

    # Initialize variables to keep track of the second largest element and its index
    second_largest = None
    second_largest_index = -1

    # Iterate through the list starting from index 40 to index 80, both inclusive
    for i in range(40, 90):
        # If the current element is greater than the second largest element, update the variables accordingly
        if my_list[i] > second_largest:
            second_largest = my_list[i]
            second_largest_index = i

    # Return the second largest element from index 40 to index 80, both inclusive
    return second_largest if second_largest_index != -1 else None
