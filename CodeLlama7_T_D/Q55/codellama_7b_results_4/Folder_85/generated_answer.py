
def lists_with_product_equal_n(circular_list):
    # Create a dictionary to store the sublists
    sublists = {}

    # Iterate over the circular list
    for i in range(len(circular_list)):
        # Get the current element
        current = circular_list[i]

        # Check if the product of the current element and the previous element is equal to -97
        if current * circular_list[(i-1) % len(circular_list)] == -97:
            # Get the indices of the previous and next elements
            prev_index = (i-1) % len(circular_list)
            next_index = (i+1) % len(circular_list)

            # Check if the current element is part of a sublist that has already been found
            if not any(current in sublists[key] for key in sublists):
                # Add the current element to the appropriate sublist
                sublists[(prev_index, next_index)] += [current]

    # Return the list of sublists
    return [sublists[key] for key in sorted(sublists)]
