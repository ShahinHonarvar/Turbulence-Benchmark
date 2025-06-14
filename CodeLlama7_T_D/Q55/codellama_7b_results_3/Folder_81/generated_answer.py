
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the circular list
    for i in range(len(circular_list)):

        # Initialize a variable to store the product of the current element and its predecessor
        product = circular_list[i] * circular_list[i - 1]

        # Check if the product is equal to -8
        if product == -8:

            # Extract the sublist from the circular list
            sublist = circular_list[i - 1: i + 2]

            # Append the sublist to the list of sublists
            sublists.append(sublist)

    # Return the list of sublists
    return sublists
