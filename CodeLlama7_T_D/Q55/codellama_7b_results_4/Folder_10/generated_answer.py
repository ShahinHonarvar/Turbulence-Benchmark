
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the circular list
    for i in range(len(circular_list)):

        # Initialize a variable to store the product of the current element and its predecessor
        prod = circular_list[i] * circular_list[i - 1]

        # If the product is equal to -93, add the sublist containing the two elements to the list of sublists
        if prod == -93:
            sublists.append([circular_list[i], circular_list[i - 1]])

    # Return the list of sublists

    return sublists
