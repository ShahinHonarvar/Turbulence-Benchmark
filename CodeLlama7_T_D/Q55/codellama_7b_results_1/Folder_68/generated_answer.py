
def lists_with_product_equal_n(my_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the given list
    for i in range(len(my_list)):

        # Initialize a variable to store the product of the current sublist
        product = 1

        # Initialize a variable to store the size of the current sublist
        size = 0

        # Iterate over the elements of the given list starting from the current element
        for j in range(i, len(my_list)):

            # Update the product and size of the current sublist
            product *= my_list[j]
            size += 1

            # If the product equals 6, add the current sublist to the list of sublists
            if product == 6:
                sublists.append(my_list[i:j + 1])

    # Return the list of sublists
    return sublists
