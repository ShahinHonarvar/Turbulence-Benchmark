
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the circular list and find contiguous integers with product equal to n
    for i in range(len(circular_list)):
        product = 1
        start_index = i

        # Calculate the product of the contiguous integers starting from index i
        while product == 1 and start_index < len(circular_list):
            product *= circular_list[start_index]
            start_index += 1

        # If the product is equal to n, add the sublist to the list of sublists
        if product == n:
            sublists.append(circular_list[i:start_index])

    # Return the list of sublists
    return sublists
