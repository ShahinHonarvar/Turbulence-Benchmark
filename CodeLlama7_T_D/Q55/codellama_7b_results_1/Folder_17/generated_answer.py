
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the circular list
    for i in range(len(circular_list)):
        # Get the current element and its index
        element = circular_list[i]
        index = i

        # Initialize a variable to store the product of the current element and its predecessors
        product = 1

        # Iterate over the elements of the circular list that come before the current element
        for j in range(index):
            # Get the previous element and its index
            prev_element = circular_list[j]
            prev_index = j

            # Multiply the product by the current element's predecessor
            product *= prev_element

        # Add the sublist of all elements with indices less than or equal to the index of the current element that have a product equal to 18 to the list of sublists
        if product == 18:
            sublists.append(circular_list[:index + 1])

    # Return the list of sublists
    return sublists
