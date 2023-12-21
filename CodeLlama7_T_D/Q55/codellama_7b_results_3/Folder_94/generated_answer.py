
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the circular list
    for i in range(len(circular_list)):

        # Initialize variables to keep track of the current sublist and its product
        current_sublist = [circular_list[i]]
        current_product = circular_list[i]

        # Iterate over the remaining elements of the circular list
        for j in range(i + 1, len(circular_list)):

            # If the product of the current sublist and the next element is equal to -30, add the next element to the current sublist
            if current_product * circular_list[j] == -30:
                current_sublist.append(circular_list[j])
                current_product = current_product * circular_list[j]

            # If the product of the current sublist and the next element is not equal to -30, then the current sublist is complete and can be added to the list of sublists
            else:
                sublists.append(current_sublist)
                break

    # Return the list of sublists that have a product of -30
    return sublists
