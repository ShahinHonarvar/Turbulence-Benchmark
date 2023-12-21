
def lists_with_product_equal_n(my_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the given list
    for i in range(len(my_list)):

        # Initialize a variable to store the product of the current element and its neighbors
        prod = 1

        # Check if the current element has a neighbor to the left
        if i > 0:

            # Multiply the product by the current element's left neighbor
            prod *= my_list[i - 1]

        # Check if the current element has a neighbor to the right
        if i < len(my_list) - 1:

            # Multiply the product by the current element's right neighbor
            prod *= my_list[i + 1]

        # Check if the product equals -3
        if prod == -3:

            # Add the sublist to the list of sublists
            sublists.append(my_list[i : i + 3])

    # Return the list of sublists
    return sublists
