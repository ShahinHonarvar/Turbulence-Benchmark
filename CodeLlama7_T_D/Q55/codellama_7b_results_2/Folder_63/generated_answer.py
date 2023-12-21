
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate through the circular list and find contiguous integers with a product equal to n

    for i in range(len(circular_list)):
        current_product = 1
        start_index = i

        while current_product == n:
            if current_product == n:
                sublists.append(circular_list[start_index:i+1])
            break

    # Return the list of sublists

    return sublists
