
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the circular list
    for i in range(len(circular_list)):
        # Initialize a variable to store the current element and its index
        current_element, current_index = circular_list[i], i
        # Initialize variables to keep track of the current product and sublist size
        current_product = 1
        current_sublist_size = 0

        # Iterate over the remaining elements of the circular list
        for j in range(i + 1, len(circular_list)):
            # Get the next element and its index
            next_element, next_index = circular_list[j], j
            # Update the current product and sublist size
            current_product *= next_element
            current_sublist_size += 1

            # If the current product equals -115, add the current sublist to the list of sublists
            if current_product == -115:
                sublists.append(circular_list[current_index:next_index])

    # Return the list of sublists
    return sublists
