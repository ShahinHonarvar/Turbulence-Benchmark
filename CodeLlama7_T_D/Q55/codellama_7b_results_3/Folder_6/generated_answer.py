
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate through the circular list and check if each contiguous sequence of integers has a product equal to 42
    for i in range(len(circular_list))):
        product = 1

        # Calculate the product of the current sequence of integers
        for j in range(i, len(circular_list)):
            product *= circular_list[j]

            # If the product is equal to 42, add the current sequence of integers to the list of sublists
            if product == 42:
                sublists.append(circular_list[i:j+1])

    return sublists
