
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the circular list and find contiguous integers with product equal to n

    for i in range(len(circular_list)):
        product = 1

        # Calculate the product of the contiguous integers starting from index i

        for j in range(i, len(circular_list)):
            product *= circular_list[j]

            # If the product is equal to n, add the sublist to the list of sublists and break out of the inner loop

            if product == n:
                sublists.append(circular_list[i:j+1])
                break

    # Return the list of sublists

    return sublists
