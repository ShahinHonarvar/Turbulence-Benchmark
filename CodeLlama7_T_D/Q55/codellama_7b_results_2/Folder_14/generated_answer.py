
def lists_with_product_equal_n(circulant_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the circulant list
    for i in range(len(circulant_list)):

        # Initialize a variable to store the product of the elements in the current sublist
        product = 1

        # Initialize a variable to store the size of the current sublist
        size = 0

        # Iterate over the remaining elements of the circulant list starting from the current element
        for j in range(i + 1, len(circulant_list)):

            # Calculate the product of the current element and the next element
            product *= circulant_list[j]

            # Increment the size of the current sublist
            size += 1

            # Check if the product is equal to -72
            if product == -72:

                # Add the current sublist to the list of sublists
                sublists.append(circulant_list[i:j + 1])

                # Break out of the inner loop since a sublist has been found
                break

    # Return the list of sublists
    return sublists
