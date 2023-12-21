
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the circular list
    for i in range(len(circular_list)):
        # Initialize a variable to store the product of the elements in the sublist
        product = 1

        # Initialize a variable to store the starting index of the sublist
        start_index = i

        # Iterate over the elements in the sublist
        for j in range(i, len(circular_list)):
            # Multiply the current element by the product variable
            product *= circular_list[j]

            # If the product equals 28, add the sublist to the list of sublists
            if product == 28:
                sublists.append(circular_list[start_index:j + 1])

                # Break out of the inner loop and move on to the next element in the circular list
                break

    # Return the list of sublists that have a product equal to 28
    return sublists
