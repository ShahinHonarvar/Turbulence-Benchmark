
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate through the circular list
    for i in range(len(circular_list)):

        # Initialize a variable to store the product of the current sublist
        product = 1

        # Initialize a variable to store the starting index of the current sublist
        start_index = i

        # Iterate through the rest of the circular list
        for j in range(i + 1, len(circular_list)):

            # Update the product and the ending index of the current sublist
            product *= circular_list[j]
            end_index = j

            # Check if the product equals 6. If it does, add the current sublist to the list of sublists
            if product == 6:
                sublists.append(circular_list[start_index:end_index + 1])

    # Return the list of sublists
    return sublists
