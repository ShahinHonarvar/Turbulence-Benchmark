
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the circular list and find contiguous integers that multiply to n

    for i in range(len(circular_list)):

        product = 1
        current_index = i

        while product == 1 and current_index < len(circular_list):

            product *= circular_list[current_index]
            current_index += 1

        if product == n:

            sublists.append(circular_list[i:current_index])

    return sublists
