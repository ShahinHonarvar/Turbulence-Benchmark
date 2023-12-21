
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements in the circular list
    for i in range(len(circular_list)):

        # Find the first element in the current sublist
        current_sublist = []

        # Iterate over the remaining elements in the circular list
        for j in range(i+1, len(circular_list)+i+1):

            # Add the current element to the current sublist
            current_sublist.append(circular_list[j % len(circular_list)])

            # Check if the product of the elements in the current sublist equals n
            if sum(current_sublist) == n:

                # Add the current sublist to the list of sublists
                sublists.append(current_sublist)

                # Break out of the inner loop since we have found a sublist that meets our criteria
                break

    # Return the list of sublists
    return sublists
