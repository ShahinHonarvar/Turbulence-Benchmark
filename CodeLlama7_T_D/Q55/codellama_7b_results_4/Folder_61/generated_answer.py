
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the circular list and find contiguous sequences of integers that have a product equal to -10
    for i in range(len(circular_list)):
        # Initialize variables to keep track of the current sequence and its product
        seq = [circular_list[i]]
        prod = seq[0]

        # Iterate over the remaining elements in the circular list
        for j in range(i + 1, len(circular_list)):
            # Add the next element to the sequence and update the product
            seq.append(circular_list[j])
            prod *= seq[-1]

            # If the product is equal to -10, add the current sequence to the list of sublists and break out of the loop
            if prod == -10:
                sublists.append(seq)
                break

    return sublists
