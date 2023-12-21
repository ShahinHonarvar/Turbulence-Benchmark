
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the circular list
    for i in range(len(circular_list)):

        # Initialize a variable to store the product of the elements in the current sublist
        product = 1

        # Initialize a variable to store the index of the current element in the circular list
        j = i

        # Iterate over the elements of the current sublist
        while product == 1 and j < len(circular_list):

            # Multiply the current element by the product variable
            product *= circular_list[j]

            # Increment the index of the current element
            j += 1

        # If the product of the elements in the current sublist is equal to 13, add it to the list of sublists
        if product == 13:
            sublists.append(circular_list[i:j])

    # Return the list of sublists
    return sublists
