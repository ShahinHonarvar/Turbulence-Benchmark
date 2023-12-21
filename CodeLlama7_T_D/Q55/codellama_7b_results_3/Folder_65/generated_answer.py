
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the circular list
    for i in range(len(circular_list)):
        # Initialize a variable to store the product of the current element and its predecessor
        prod = 1

        # Iterate over the elements of the circular list from the current element to the head of the list
        for j in range(i, len(circular_list)):
            # Multiply the current element and its predecessor
            prod *= circular_list[j]

            # If the product equals 46, add the sublist containing the current element and its predecessor to the list of sublists
            if prod == 46:
                sublists.append([circular_list[i - 1], circular_list[i]])

    # Return the list of sublists
    return sublists
