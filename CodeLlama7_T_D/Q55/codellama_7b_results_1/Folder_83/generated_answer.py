
def lists_with_product_equal_n(circul_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the circular list
    for i in range(len(circul_list)):
        # Get the current element and its successor
        current_element = circul_list[i]
        next_element = circul_list[(i+1) % len(circul_list)]

        # Check if the product of the current element and its successor is equal to -57
        if current_element * next_element == -57:
            # If it is, add the sublist containing the current element and its successor to the list of sublists
            sublists.append([current_element, next_element])

    # Return the list of sublists
    return sublists
