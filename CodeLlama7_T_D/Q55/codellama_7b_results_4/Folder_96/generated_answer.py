
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate through the circular list and find contiguous sequences of integers with product equal to n

    for i in range(len(circular_list)):
        # Initialize variables to keep track of the current sequence and its product
        curr_seq = [circular_list[i]]
        curr_prod = circular_list[i]

        # Iterate through the remaining elements of the circular list

        for j in range(i + 1, len(circular_list)):
            # If the product of the current sequence and the next element is equal to n, add the next element to the current sequence

            if curr_prod * circular_list[j] == n:
                curr_seq.append(circular_list[j])
                curr_prod = curr_prod * circular_list[j]

            # If the product of the current sequence and the next element is not equal to n, add the current sequence to the list of sublists and reset the variables

            else:
                sublists.append(curr_seq)
                curr_seq = [circular_list[j]]
                curr_prod = circular_list[j]

        # Add the final sequence to the list of sublists

        sublists.append(curr_seq)

    # Return the list of sublists

    return sublists
