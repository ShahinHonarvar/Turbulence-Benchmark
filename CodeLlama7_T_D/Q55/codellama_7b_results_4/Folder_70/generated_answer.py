
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the circular list and find contiguous integers whose product equals 32
    for i in range(len(circular_list)):
        # Initialize a variable to store the product of the current contiguous integers
        product = 1

        # Calculate the product of the current contiguous integers
        for j in range(i, len(circular_list)):
            product *= circular_list[j]

            # If the product equals 32, add the sublist to the list of sublists
            if product == 32:
                sublists.append(circular_list[i:j+1])

                # If there are duplicates of such a sublist, they should all be contained in the returned list. The order of sublists in the returned list does not matter.
        if len(sublists) > 0:
            return sublists

    # If no such sublist exists, the function should return an empty list.
    else:
        return []
