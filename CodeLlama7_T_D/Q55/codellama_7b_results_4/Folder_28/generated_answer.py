
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the circular list and find contiguous integers with a product equal to n

    for i in range(len(circular_list)):
        current_product = 1
        start_index = i

        while current_product == n:
            current_product *= circular_list[i]
            i += 1

            if i >= len(circular_list):
                i = 0

        # If the product is equal to n, add the sublist to the list of sublists

        if current_product == n:
            sublists.append(circular_list[start_index:i])

    # Return the list of sublists

    return sublists
