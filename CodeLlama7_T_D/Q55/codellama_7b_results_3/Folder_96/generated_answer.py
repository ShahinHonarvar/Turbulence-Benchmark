
def lists_with_product_equal_n(circular_list):
    # Find the product of all elements in the list
    product = 1
    for element in circular_list:
        product *= element

    # Create an empty list to store the sublists
    sublists = []

    # Iterate through the list and find contiguous sequences of elements that have a product equal to n
    current_sequence = []
    for element in circular_list:
        if product / element == 1:
            # If the sequence is not empty, add it to the sublists list
            if current_sequence:
                sublists.append(current_sequence)

            # Reset the sequence and the product
            current_sequence = []
            product = 1
        else:
            # Add the element to the sequence
            current_sequence.append(element)

    # If there are any elements left in the sequence, add them to the sublists list
    if current_sequence:
        sublists.append(current_sequence)

    return sublists
