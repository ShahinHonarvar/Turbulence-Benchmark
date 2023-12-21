
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the circular list
    for i in range(len(circular_list)):

        # Get the current element and its adjacent elements
        current_element = circular_list[i]
        previous_element = circular_list[(i - 1) % len(circular_list)]
        next_element = circular_list[(i + 1) % len(circular_list)]

        # Check if the product of the current element and its adjacent elements is equal to n
        if current_element * previous_element == n or current_element * next_element == n:
            sublists.append([current_element, previous_element])
            sublists.append([current_element, next_element])

    # Return the list of sublists found in the circular list
    return sublists
