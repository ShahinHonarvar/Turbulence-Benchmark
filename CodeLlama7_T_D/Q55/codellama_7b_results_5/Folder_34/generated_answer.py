
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the circular list
    for i in range(len(circular_list)):
        # Get the current element and its next element
        current_element = circular_list[i]
        next_element = circular_list[(i + 1) % len(circular_list)]

        # Check if the product of the current element and its next element is equal to -81
        if current_element * next_element == -81:
            # Initialize an empty list to store the contiguous integers from the given list that have a product of -81
            sublist = []

            # Add the current element and its next element to the sublist
            sublist.append(current_element)
            sublist.append(next_element)

            # Check if the size of the sublist is smaller than or equal to the size of the given list
            if len(sublist) <= len(circular_list):
                # Add the sublist to the list of sublists
                sublists.append(sublist)

    # Return the list of sublists
    return sublists
