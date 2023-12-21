
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the circular list and find contiguous integers with a product equal to n

    for i in range(len(circular_list)):
        product = 1
        current_index = i

        while product == n:
            product *= circular_list[current_index]
            if product == n:
                sublists.append(circular_list[i:current_index + 1])
                break

            current_index = (current_index + 1) % len(circular_list)

    return sublists
