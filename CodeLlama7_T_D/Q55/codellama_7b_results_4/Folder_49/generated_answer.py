
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Loop through the elements of the circular list
    for i in range(len(circular_list)):
        # Initialize a variable to store the product of the elements in the current sublist
        product = 1

        # Loop through the remaining elements of the circular list, starting from the next element after the current one
        for j in range(i + 1, len(circular_list)):
            # Multiply the current product by the next element
            product *= circular_list[j]

            # If the product equals -61, add the sublist to the list of sublists and break out of the inner loop
            if product == -61:
                sublists.append(circular_list[i:j + 1])
                break

    # Return the list of sublists
    return sublists
