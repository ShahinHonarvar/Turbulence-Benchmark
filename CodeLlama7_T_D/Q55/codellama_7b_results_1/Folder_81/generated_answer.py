
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the circular list
    for i in range(len(circular_list))):
        # Initialize a variable to store the product of the current sublist
        product = 1

        # Iterate over the elements of the current sublist
        for j in range(i, len(circular_list)))
            # Update the product of the current sublist with the element at the current index
            product *= circular_list[j]

        # Check if the product of the current sublist equals -8
        if product == -8:
            # Add the current sublist to the list of sublists
            sublists.append(circular_list[i:j+1])

    # Return the list of sublists
    return sublists
