
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the circular list
    for i in range(len(circular_list)):

        # Initialize a variable to keep track of the current product
        current_product = 1

        # Initialize a variable to keep track of the size of the current sublist
        current_sublist_size = 0

        # Iterate over the elements of the circular list starting from the current element
        for j in range(i, len(circular_list)):

            # Calculate the product of the current element and all previous elements in the sublist
            current_product *= circular_list[j]

            # Increment the size of the current sublist by 1
            current_sublist_size += 1

            # Check if the product is equal to -41, if yes then add the sublist to the list of sublists
            if current_product == -41:
                sublists.append(circular_list[i:j + 1])
                break

        # If the size of the current sublist is greater than or equal to the size of the given list, then break the loop
        if current_sublist_size >= len(circular_list):
            break

    # Return the list of sublists
    return sublists
