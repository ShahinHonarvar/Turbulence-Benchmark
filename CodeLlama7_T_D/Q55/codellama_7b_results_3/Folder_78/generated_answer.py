
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the circular list
    for i in range(len(circular_list)):

        # Get the current element and its next element
        # If the next element is not None, then it is also part of the current sublist
        current_element = circular_list[i]
        next_element = circular_list[(i + 1) % len(circular_list)] if i < len(circular_list) - 1 else None

        # If the current element is not None and its product with the next element equals 74, then add it to the sublists list
        if current_element is not None and current_element * next_element == 74:
            sublists.append([current_element, next_element])

    # Return the sublists list
    return sublists
