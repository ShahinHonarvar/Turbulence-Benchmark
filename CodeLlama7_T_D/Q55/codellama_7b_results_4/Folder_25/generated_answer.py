
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the circular list and find contiguous integers whose product is equal to -32
    for i in range(len(circular_list)):
        current_product = 1
        start_index = i

        # Iterate over the remaining elements of the circular list
        for j in range(i + 1, len(circular_list) + 1):
            current_product *= circular_list[j % len(circular_list)]

            # If the product is equal to -32, add the sublist to the list of sublists
            if current_product == -32:
                sublists.append(circular_list[start_index:j])

                # Reset the product and start index for the next sublist
                current_product = 1
                start_index = j

    return sublists
