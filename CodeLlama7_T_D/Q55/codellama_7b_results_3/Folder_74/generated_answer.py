
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the circular list
    for i in range(len(circular_list)):

        # Initialize a variable to store the product of the current sublist
        product = 1

        # Initialize a variable to store the starting index of the current sublist
        start_index = i

        # Iterate over the elements of the circular list from the current index to the end of the list
        for j in range(i, len(circular_list)):

            # Update the product of the current sublist with the element at the current index
            product *= circular_list[j]

            # If the product equals n, add the sublist to the list of sublists and reset the product and starting index variables
            if product == n:
                sublists.append(circular_list[start_index:j+1])
                product = 1
                start_index = j + 1

    # Return the list of sublists
    return sublists
