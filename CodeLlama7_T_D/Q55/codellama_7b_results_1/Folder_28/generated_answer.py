
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate through the circular list and find contiguous integers that multiply to 85
    for i in range(len(circular_list)):
        product = 1
        start_index = i

        while product <= 85:
            product *= circular_list[i]
            i += 1

            if i == len(circular_list):
                i = 0

        # If the product is equal to 85, add the contiguous integers to the sublists list
        if product == 85:
            sublists.append(circular_list[start_index:i])

    return sublists
