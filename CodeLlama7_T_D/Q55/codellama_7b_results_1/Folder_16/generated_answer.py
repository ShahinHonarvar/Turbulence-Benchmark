
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate through the circular list and find all contiguous integers with product equal to -837
    for i in range(len(circular_list)):
        current_product = 1
        start_index = i

        # Calculate the product of the contiguous integers starting from index i
        while current_product == 1 and start_index < len(circular_list):
            current_product *= circular_list[start_index]
            start_index += 1

        # If the product is equal to -837, add the sublist to the list of sublists
        if current_product == -837:
            sublists.append(circular_list[i:start_index])

    return sublists
