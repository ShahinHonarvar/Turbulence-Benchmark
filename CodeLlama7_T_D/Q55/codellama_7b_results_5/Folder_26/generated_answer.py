
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the circular list
    for i in range(len(circular_list))

        # If the current element is 93, add it to the current sublist
        if circular_list[i] == 93:
            sublists[-1].append(circular_list[i])

        # Otherwise, start a new sublist with the current element
        else:
            sublists.append([circular_list[i]])

    # Return the list of sublists that have a product equal to 93
    return sublists
