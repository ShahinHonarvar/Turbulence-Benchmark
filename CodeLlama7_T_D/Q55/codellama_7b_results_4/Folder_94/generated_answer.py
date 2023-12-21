
def lists_with_product_equal_n(my_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the given list
    for i in range(len(my_list)):

        # Initialize a variable to store the product of the current element and its adjacent elements
        prod = 1

        # Iterate over the remaining elements of the given list starting from the current element
        for j in range(i + 1, len(my_list)):

            # Multiply the current element and its adjacent elements to get their product
            prod *= my_list[j]

            # If the product equals -30, add the sublist of contiguous integers from the given list that starts at the current element and ends at the index of the element where the product equals -30 to the returned list
            if prod == -30:
                sublists.append(my_list[i:j])

    # Return the list of sublists each of which contains the contiguous integers from the given list such that their product equals -30
    return sublists
