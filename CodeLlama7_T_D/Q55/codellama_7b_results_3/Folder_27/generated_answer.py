 def lists_with_product_equal_n(my_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Loop through the elements of the given list
    for i in range(len(my_list)):

        # Initialize a variable to store the product of the contiguous elements from the current index
        prod = 1

        # Initialize a variable to store the size of the sublist being constructed
        size = 0

        # Loop through the remaining elements of the given list
        for j in range(i, len(my_list)):

            # Update the product of the contiguous elements and the size of the sublist
            prod *= my_list[j]
            size += 1

            # If the product equals -82, add the sublist to the list of sublists and break out of the loop
            if prod == -82:
                sublists.append(my_list[i:j + 1])
                break

    # Return the list of sublists or an empty list if no such sublist exists
    return sublists if sublists else []
