
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []
    # Iterate over the elements of the circular list
    for i in range(len(circular_list)):
        # Initialize a variable to store the product of the elements in the current sublist
        product = 1
        # Initialize a variable to store the index of the last element in the current sublist
        j = i

        # While the product of the elements in the current sublist is equal to -16, continue iterating over the elements of the circular list
        while product == -16:
            # Multiply the current element by the product variable
            product *= circular_list[j]

            # If the product variable is equal to -16, add the current sublist to the returned list
            if product == -16:
                sublists.append(circular_list[i:j + 1])

            # Increment the index of the last element in the current sublist by 1
            j += 1

        # If the product variable is not equal to -16, reset the product variable and continue iterating over the elements of the circular list
        if product != -16:
            product = 1
            i += 1

    # Return the list of sublists that have a product of their elements equal to -16
    return sublists
