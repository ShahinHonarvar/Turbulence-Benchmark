
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate through the circular list and find contiguous integers with a product equal to n
    for i in range(len(circular_list)):
        product = 1

        # Calculate the product of the current element and all subsequent elements
        for j in range(i, len(circular_list)):
            product *= circular_list[j]

            # If the product is equal to n, add the sublist to the list of sublists
            if product == n:
                sublists.append(circular_list[i:j+1])

    # Return the list of sublists
    return sublists
