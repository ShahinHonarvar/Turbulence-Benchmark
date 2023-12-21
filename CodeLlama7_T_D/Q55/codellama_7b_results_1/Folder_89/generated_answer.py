
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate through the circular list and find contiguous sequences of integers whose product equals n (57)
    for i in range(len(circular_list)):
        product = 1

        # Calculate the product of the sequence of integers starting from index i
        for j in range(i, len(circular_list)):
            product *= circular_list[j]

            # If the product equals n (57), add the sequence to the list of sublists
            if product == 57:
                sublists.append(circular_list[i:j+1])
                break

    return sublists
