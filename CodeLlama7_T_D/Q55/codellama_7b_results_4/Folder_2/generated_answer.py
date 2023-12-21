
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the circular list
    for i in range(len(circular_list)):

        # Get the current element and its index in the circular list
        current_element = circular_list[i]
        current_index = i

        # Initialize a variable to store the product of the elements in the sublist
        sublist_product = 1

        # Iterate over the remaining elements in the circular list
        for j in range(i + 1, len(circular_list)):

            # Get the next element and its index in the circular list
            next_element = circular_list[j]
            next_index = j

            # Update the product of the elements in the sublist
            sublist_product *= next_element

            # Check if the product equals -968
            if sublist_product == -968:

                # Add the current sublist to the list of sublists
                sublists.append(circular_list[current_index:next_index + 1])

                # Update the product of the elements in the sublist
                sublist_product = 1

    # Return the list of sublists
    return sublists
