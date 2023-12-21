
def lists_with_product_equal_n(circlist):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the given circular list
    for i in range(len(circlist)):
        # Initialize a variable to store the product of the elements in the current sublist
        product = 1

        # Initialize a variable to store the starting index of the current sublist
        start_index = i

        # Iterate over the remaining elements of the given circular list
        for j in range(i+1, len(circlist)):
            # Update the product of the elements in the current sublist
            product *= circlist[j]

            # Check if the product of the elements in the current sublist equals -15
            if product == -15:
                # Add the current sublist to the list of sublists
                sublists.append(circlist[start_index:j+1])

    # Return the list of sublists
    return sublists
