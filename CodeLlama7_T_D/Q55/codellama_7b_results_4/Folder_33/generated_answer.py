
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the circular list
    for i in range(len(circular_list)):

        # Initialize variables to keep track of the current sublist and its product
        current_sublist = [circular_list[i]]
        current_product = circular_list[i]

        # Iterate over the remaining elements of the circular list
        for j in range(i+1, len(circular_list)):

            # Add the current element to the current sublist if its product with the previous element is equal to -115
            if (current_product * circular_list[j]) == -115:
                current_sublist.append(circular_list[j])
                current_product = current_product * circular_list[j]

            # If the product of the current element with the previous element is not equal to -115, then we have found a sublist that meets our criteria and we can break out of the inner loop
            else:
                break

        # If the current sublist is not empty, then we have found a sublist that meets our criteria and we can add it to the returned list
        if current_sublist:
            sublists.append(current_sublist)

    # Return the list of sublists that meet our criteria
    return sublists
