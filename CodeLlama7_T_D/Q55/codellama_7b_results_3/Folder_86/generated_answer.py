
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the circular list and find contiguous integers with product equal to -779
    for i in range(len(circular_list))
        product = 1
        start_index = i

        while product == -779:
            product *= circular_list[i]
            i += 1

            if i >= len(circular_list):
                i = 0

        # Add the contiguous integers with product equal to -779 to the sublists list
        sublists.append(circular_list[start_index:i])

    return sublists
