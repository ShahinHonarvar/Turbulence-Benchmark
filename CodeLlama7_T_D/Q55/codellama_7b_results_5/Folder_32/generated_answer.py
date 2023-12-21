
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the circular list
    for i in range(len(circular_list)):

        # Initialize a variable to store the product of the elements in the current sublist
        product = 1

        # Initialize a variable to store the size of the current sublist
        size = 0

        # Iterate over the remaining elements of the circular list starting from the current element
        for j in range(i, len(circular_list)):

            # Calculate the product of the elements in the current sublist
            product *= circular_list[j]

            # Increment the size of the current sublist
            size += 1

            # Check if the product equals 76. If it does, add the current sublist to the list of sublists and break out of the loop.
            if product == 76:
                sublists.append(circular_list[i:j + 1])
                break

    # Return the list of sublists
    return sublists
