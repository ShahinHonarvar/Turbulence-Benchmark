
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Loop through each element of the circular list
    for i in range(len(circular_list)):
        # Initialize a variable to store the product of the current element and its predecessor
        prod = 1

        # Calculate the product of the current element and its predecessor
        if i > 0:
            prod *= circular_list[i - 1]

        # Initialize a variable to store the current sublist
        sublist = []

        # Loop through each element of the circular list starting from the current element
        for j in range(i, len(circular_list)):
            # Calculate the product of the current element and its predecessor
            prod *= circular_list[j]

            # Check if the product equals -95
            if prod == -95:
                # Add the current sublist to the list of sublists
                sublists.append(sublist)

                # Break out of the inner loop
                break

            # If the product does not equal -95, add the current element to the current sublist
            else:
                sublist.append(circular_list[j])

    # Return the list of sublists
    return sublists
