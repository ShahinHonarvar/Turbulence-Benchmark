
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the circular list
    for i in range(len(circular_list)):
        # Initialize a variable to store the product of the current element and its predecessor
        prod = 1

        # Iterate over the remaining elements of the circular list, starting from the current element
        for j in range(i + 1, len(circular_list)):
            # Calculate the product of the current element and its predecessor
            prod *= circular_list[j]

            # If the product equals -23, add the sublist containing the contiguous integers from the given list to the returned list
            if prod == -23:
                sublists.append(circular_list[i:j + 1])

    # Return the list of sublists found, or an empty list if no such sublists exist
    return sublists
