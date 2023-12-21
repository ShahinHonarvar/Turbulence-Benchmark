
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the circular list and find contiguous integers with product equal to n

    for i in range(len(circular_list)):
        # Initialize variables to keep track of the current contiguous sequence and its product
        curr_seq = [circular_list[i]]
        curr_prod = circular_list[i]

        # Iterate over the remaining elements of the circular list

        for j in range(i + 1, len(circular_list)):
            # If the product of the current sequence and the next element is equal to n, then add the current sequence to the sublists list and reset the current sequence
            if curr_prod * circular_list[j] == n:
                sublists.append(curr_seq)
                curr_seq = []

            # Add the next element to the current sequence
            curr_seq.append(circular_list[j])

            # Update the product of the current sequence
            curr_prod *= circular_list[j]

    # Return the list of sublists with their products equal to n
    return sublists
