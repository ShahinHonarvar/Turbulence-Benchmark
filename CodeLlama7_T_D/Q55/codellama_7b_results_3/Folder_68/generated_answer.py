
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the circular list
    for i in range(len(circular_list)):
        # Initialize a variable to store the product of the elements in the current sublist
        product = 1

        # Iterate over the elements in the current sublist
        for j in range(i, len(circular_list)):
            # Update the product of the elements in the current sublist
            product *= circular_list[j]

            # If the product equals 6, add the current sublist to the list of sublists
            if product == 6:
                sublists.append(circular_list[i:j+1])

            # If the product is greater than 6, break out of the inner loop
            elif product > 6:
                break

    # Return the list of sublists
    return sublists
