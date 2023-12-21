
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate through the circular list and find contiguous sequences of integers that have a product equal to -36. Each such sequence is added to the list of sublists
    for i in range(len(circular_list))):
        current_product = 1
        current_sum = 0
        start_index = i
        while current_product == -36 and i < len(circular_list)):
            current_product *= circular_list[i]
            current_sum += circular_list[i]
            i += 1

        # If the product is equal to -36, add the corresponding sublist to the list of sublists
        if current_product == -36:
            sublists.append(circular_list[start_index:i])

    return sublists
