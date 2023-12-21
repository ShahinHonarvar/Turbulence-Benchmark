
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements in the circular list
    for i in range(len(circular_list)):
        # Initialize an empty list to store the current sublist
        current_sublist = []

        # Add the current element to the current sublist
        current_sublist.append(circular_list[i])

        # Iterate over the remaining elements in the circular list
        for j in range(i+1, len(circular_list)):
            # If the product of the current sublist and the next element is equal to -22, add the next element to the current sublist and continue iterating over the remaining elements
            if (current_sublist[-1] * circular_list[j]) == (-22)):
                current_sublist.append(circular_list[j])

    # Return the list of sublists that have a product equal to -22
    return sublists
