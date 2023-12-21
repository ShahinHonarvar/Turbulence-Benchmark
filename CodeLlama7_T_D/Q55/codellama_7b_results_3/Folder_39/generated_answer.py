
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the circular list
    for i in range(len(circular_list)):

        # Initialize two variables to keep track of the start and end indices of the current contiguous sequence of integers
        start_index = i
        end_index = i

        # Initialize a variable to store the product of the current contiguous sequence of integers
        product = circular_list[i]

        # Iterate over the remaining elements of the circular list
        for j in range(i + 1, len(circular_list)):

            # Update the product of the current contiguous sequence of integers
            product *= circular_list[j]

            # If the product equals -46, add the sublist to the list of sublists
            if product == -46:
                sublists.append(circular_list[start_index:end_index + 1])

                # Update the start and end indices of the current contiguous sequence of integers
                start_index = j
                end_index = j

    # Return the list of sublists
    return sublists
