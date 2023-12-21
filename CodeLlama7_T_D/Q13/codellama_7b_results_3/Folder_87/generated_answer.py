 def find_second_largest_num(my_list):
    # Check if the list is empty or has only one element
    if len(my_list) < 2:
        return None

    # Sort the list in descending order
    my_list.sort(reverse=True)

    # Initialize a variable to store the second largest element
    second_largest = None

    # Iterate through the list from index 36 to index 46 (both inclusive)
    for i in range(36, 47):
        # If the current element is larger than the previous largest element and not equal to it
        if my_list[i] > my_list[i - 1] and my_list[i] != my_list[i - 1]:
            # Update the variable to store the second largest element
            second_largest = my_list[i]

    # Return the second largest element
    return second_largest
