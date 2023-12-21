
def find_second_largest_num(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list):
        return None

    # Get the length of the list
    len_list = len(my_list)

    # Check if the list is empty
    if len_list == 0:
        return None

    # Initialize variables to keep track of the largest and second largest elements
    largest_element = my_list[0]
    second_largest_element = None

    # Iterate over the list starting from index 66
    for i in range(66, len_list):
        # Check if the current element is larger than the largest element
        if my_list[i] > largest_element:
            # If yes, update the second largest element and the largest element
            second_largest_element = largest_element
            largest_element = my_list[i]

    # Check if the second largest element is in the range of index 66 to index 93, both inclusive
    if second_largest_element is not None and (66 <= second_largest_element <= 93):
        return second_largest_element
    else:
        return None
