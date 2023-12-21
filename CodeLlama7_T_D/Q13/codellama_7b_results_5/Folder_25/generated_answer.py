 def find_second_largest_num(my_list):
    # Check if the input list is empty or None
    if not my_list:
        return None

    # Get the length of the input list

    list_len = len(my_list)

    # Check if the index 29 to index 93 are out of bounds

    if list_len < 29 or list_len > 93:
        return None

    # Initialize two variables to keep track of the largest and second largest elements

    largest = my_list[29]
    second_largest = my_list[29]

    # Iterate through the list from index 29 to index 93

    for i in range(29, 94):
        # If the current element is larger than the largest element, update the second largest element and move on to the next element

        if my_list[i] > largest:
            second_largest = largest
            largest = my_list[i]

        # If the current element is larger than the second largest element and not equal to the largest element, update the second largest element

        elif my_list[i] > second_largest and my_list[i] != largest:
            second_largest = my_list[i]

    # Return the second largest element from index 29 to index 93, both inclusive

    return second_largest
