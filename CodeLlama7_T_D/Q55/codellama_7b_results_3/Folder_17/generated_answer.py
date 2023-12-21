
def lists_with_product_equal_n(my_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the given list
    for i in range(len(my_list)):

        # Initialize a variable to store the product of the elements in the current sublist
        product = 1

        # Initialize a variable to store the size of the current sublist
        size = 0

        # Iterate over the elements of the given list starting from the current element
        for j in range(i, len(my_list)):

            # Update the product of the elements in the current sublist
            product *= my_list[j]

            # Increment the size of the current sublist
            size += 1

            # Check if the product of the elements in the current sublist is equal to 18
            if product == 18:

                # Add the current sublist to the list of sublists
                sublists.append(my_list[i:j+1])

                # Break out of the inner loop
                break

    return sublists
