
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate through the elements of the circular list
    for i in range(len(circular_list)):
        # Get the current element and its index
        current_element = circular_list[i]
        current_index = i

        # Initialize a variable to store the product of the current sublist
        product = 1

        # Iterate through the remaining elements of the circular list
        for j in range(i + 1, len(circular_list)):
            # Get the next element and its index
            next_element = circular_list[j]
            next_index = j

            # Update the product of the current sublist
            product *= next_element

            # Check if the product is equal to -54
            if product == -54:
                # Add the sublist to the list of sublists
                sublists.append(circular_list[current_index:next_index + 1])

    # Return the list of sublists
    return sublists
