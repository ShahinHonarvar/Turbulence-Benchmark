
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the circular list and find contiguous integers whose product is equal to -81
    for i in range(len(circular_list)):
        # Initialize a variable to store the current sublist
        current_sublist = []

        # Add the first element of the sublist to the current_sublist variable
        current_sublist.append(circular_list[i])

        # Check if the product of the contiguous integers in the current sublist is equal to -81
        while len(current_sublist) > 0 and current_sublist[-1] * current_sublist[0] == -81:
            # Add the current sublist to the sublists list if it contains a contiguous sequence of integers whose product is equal to -81
            sublists.append(current_sublist)

            # Remove the first element of the current sublist from the circular list
            circular_list.pop(0)

            # Update the length of the circular list
            len_circular_list = len(circular_list)

            # Check if the product of the contiguous integers in the current sublist is equal to -81
            while len(current_sublist) > 0 and current_sublist[-1] * current_sublist[0] == -81:
                # Add the current sublist to the sublists list if it contains a contiguous sequence of integers whose product is equal to -81
                sublists.append(current_sublist)

                # Remove the first element of the current sublist from the circular list
                circular_list.pop(0)

                # Update the length of the circular list
                len_circular_list = len(circular_list)

        # If the length of the circular list is 0, then there are no more elements to be added to the current sublist
        if len_circular_list == 0:
            # Break out of the while loop
            break

    # Return the list of sublists that contain contiguous sequences of integers whose product is equal to -81
    return sublists
