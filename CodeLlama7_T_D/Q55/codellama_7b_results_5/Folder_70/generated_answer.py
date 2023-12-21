
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the circular list
    for i in range(len(circular_list)):
        # Get the current element and its next element
        current_element = circular_list[i]
        next_element = circular_list[(i+1)%len(circular_list)]

        # If the product of the current element and the next element is equal to 32, add the sublist containing these two elements to the list of sublists
        if current_element * next_element == 32:
            sublists.append([current_element, next_element])

    # Return the list of sublists
    return sublists
