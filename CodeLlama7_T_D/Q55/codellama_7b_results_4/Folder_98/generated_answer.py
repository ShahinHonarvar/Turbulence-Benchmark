
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the circular list
    for i in range(len(circular_list)):
        # Get the current element and its next element
        current_element = circular_list[i]
        next_element = circular_list[(i+1)%len(circular_list)]

        # Check if the product of the current element and the next element is equal to -1
        if current_element * next_element == -1:
            # Initialize an empty list to store the contiguous integers from the circular list
            sublist = []

            # Append the current element to the sublist
            sublist.append(current_element)

            # Iterate over the elements of the circular list starting from the next element
            for j in range((i+1)%len(circular_list)), len(circular_list)):
                # Get the current element and its previous element
                current_element = circular_list[j]
                previous_element = circular_list[(j-1)%len(circular_list)]

                # Check if the product of the current element and the previous element is equal to -1
                if current_element * previous_element == -1:
                    # Append the current element to the sublist
                    sublist.append(current_element)

            # Add the sublist to the list of sublists
            sublists.append(sublist)

    # Return the list of sublists
    return sublists
