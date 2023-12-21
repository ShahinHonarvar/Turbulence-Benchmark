
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the circular list
    for i in range(len(circular_list)):
        # Get the current element and its adjacent elements
        curr_element = circular_list[i]
        left_adjacent_elements = circular_list[i-1:i]
        right_adjacent_elements = circular_list[i+1:i+2]

        # Calculate the product of the current element and its adjacent elements
        product = curr_element * (left_adjacent_elements + right_adjacent_elements)

        # If the product is equal to -69, add the current sublist to the list of sublists
        if product == -69:
            sublists.append(circular_list[i-1:i+2])

    # Return the list of sublists
    return sublists
