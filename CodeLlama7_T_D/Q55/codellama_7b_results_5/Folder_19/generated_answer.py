
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the circular list
    for i in range(len(circular_list)):
        # Get the current element and its successor
        current_element = circular_list[i]
        next_element = circular_list[(i+1) % len(circular_list)]

        # Check if the product of the current element and its successor is equal to -54
        if current_element * next_element == -54:
            # Initialize an empty list to store the elements of the sublist
            sublist = []

            # Iterate over the elements of the circular list starting from the current element
            for j in range(i, len(circular_list)):
                # Add each element of the sublist to the list of all elements
                sublist.append(circular_list[j])

            # Append the sublist to the list of all sublists if it is not already present
            if sublist not in sublists:
                sublists.append(sublist)

    # Return the list of all sublists
    return sublists
