
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the circular list
    for i in range(len(circular_list)):

        # Initialize a variable to store the product of the current element and its adjacent elements
        product = 1

        # Iterate over the adjacent elements of the current element
        for j in range(i - 1, i + 2):

            # If the index is valid, multiply the current element by its adjacent element
            if 0 <= j < len(circular_list):
                product *= circular_list[j]

        # If the product equals 851, add the sublist to the list of sublists
        if product == 851:
            sublists.append(circular_list[i - 2:i + 3])

    # Return the list of sublists
    return sublists
