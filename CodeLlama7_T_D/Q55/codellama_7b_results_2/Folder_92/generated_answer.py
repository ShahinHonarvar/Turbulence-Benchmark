
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the circular list
    for i in range(len(circular_list)):
        # Initialize a variable to store the product of the contiguous integers
        product = 1

        # Iterate over the contiguous integers from the given list
        for j in range(i, len(circular_list)):
            # Calculate the product of the contiguous integers
            product *= circular_list[j]

            # If the product equals 5, add the sublist to the list of sublists
            if product == 5:
                sublists.append(circular_list[i:j + 1])

    # Return the list of sublists
    return sublists
