
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the circular list
    for i in range(len(circular_list))
        # Initialize a variable to store the current product
        current_product = 1

        # Iterate over the remaining elements of the circular list
        for j in range(i + 1, len(circular_list))
            # Update the current product with the product of the current element and the next element
            current_product *= circular_list[j]

            # If the current product is equal to n, add the sublist to the list of sublists
            if current_product == n:
                sublists.append(circular_list[i:j + 1])

        # Reset the current product to 1 for the next iteration
        current_product = 1

    # Return the list of sublists
    return sublists
