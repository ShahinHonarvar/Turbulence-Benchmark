
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the circular list
    for i in range(len(circular_list)):

        # Get the current element and its index in the list
        element = circular_list[i]
        index = i

        # Initialize a variable to store the product of the elements in the sublist
        product = 1

        # Iterate over the elements of the sublist
        for j in range(index, len(circular_list)):

            # Get the current element and its index in the list
            current_element = circular_list[j]
            current_index = j

            # If the product of the elements in the sublist is equal to 32, add the sublist to the list of sublists
            if product == 32:
                sublists.append(circular_list[index:current_index + 1])

            # Increment the product by the current element
            product *= current_element

    # Return the list of sublists
    return sublists
