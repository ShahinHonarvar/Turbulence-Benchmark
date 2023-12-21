
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the circular list and calculate the product of contiguous integers
    for i in range(len(circular_list))):
        product = 1
        for j in range(i, len(circular_list)):
            product *= circular_list[j]
            if product == 51:
                # Add the sublist to the list of sublists
                sublists.append(circular_list[i:j+1])
                break

    return sublists
