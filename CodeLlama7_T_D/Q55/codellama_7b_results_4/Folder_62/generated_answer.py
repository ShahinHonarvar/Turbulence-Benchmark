
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate through the circular list and find contiguous sequences of integers that multiply to 100
    for i in range(len(circular_list)):
        # Initialize variables to keep track of the current product and the length of the current sequence
        current_product = 1
        current_sequence_length = 0

        # Iterate through the remaining elements in the circular list, starting from the current index
        for j in range(i + 1, len(circular_list) + 1):
            # Calculate the product of the current sequence and the next element in the circular list
            current_product *= circular_list[(j - 1) % len(circular_list)]

            # If the product is equal to 100, add the current sequence to the list of sublists
            if current_product == 100:
                sublists.append(circular_list[i:j])

                # Update the current sequence length and reset the product
                current_sequence_length = j - i
                current_product = 1

    # Return the list of sublists that were found
    return sublists
