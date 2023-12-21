
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the circular list
    for i in range(len(circular_list)):
        # Initialize a variable to store the product of the elements in the current sublist
        product = 1

        # Add the current element to the current sublist
        current_sublist = [circular_list[i]]

        # Iterate over the remaining elements of the circular list
        for j in range(i + 1, len(circular_list)):
            # Update the product of the elements in the current sublist
            product *= circular_list[j]

            # Add the current element to the current sublist if its product with the previous element is equal to n
            if product == n:
                current_sublist.append(circular_list[j])

        # Add the current sublist to the list of sublists if it is not empty
        if len(current_sublist) > 0:
            sublists.append(current_sublist)

    # Return the list of sublists
    return sublists
