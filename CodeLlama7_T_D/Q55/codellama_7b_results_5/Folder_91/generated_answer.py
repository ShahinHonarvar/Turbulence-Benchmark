
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the circular list and find contiguous integers with product equal to 2
    for i in range(len(circular_list)):
        current_product = 1
        current_sum = 0
        start_index = i

        while current_product == 2:
            current_sum += circular_list[i]
            if current_sum > 2:
                break

            current_product *= circular_list[i]
            i += 1

        # If the product is equal to 2, add the sublist to the list of sublists
        if current_product == 2:
            sublists.append(circular_list[start_index:i]))

    return sublists
