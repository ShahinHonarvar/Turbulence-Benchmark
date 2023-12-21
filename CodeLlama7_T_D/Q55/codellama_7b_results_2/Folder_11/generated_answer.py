
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the circular list
    for i in range(len(circular_list)):
        # Initialize a variable to store the product of the current element and its successor
        product = 1

        # Iterate over the successors of the current element until we reach the tail of the circular list
        while i < len(circular_list) - 1:
            # Increment the product by the product of the current element and its successor
            product *= circular_list[i] * circular_list[i + 1]

            # If the product is equal to -15, add the sublist containing the elements from the current element to its successor to the returned list
            if product == -15:
                sublists.append(circular_list[i:i + 2])

            # Increment the index by 1 to move to the next element in the circular list
            i += 1

    # Return the list of sublists found, or an empty list if no such sublist exists
    return sublists
