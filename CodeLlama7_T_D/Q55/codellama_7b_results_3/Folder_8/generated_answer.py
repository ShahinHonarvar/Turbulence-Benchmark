
def lists_with_product_equal_n(circular_list):
    # Check if the list is empty
    if not circular_list:
        return []

    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the circular list
    for i in range(len(circular_list)):
        # Get the current element and its predecessor
        current_element = circular_list[i]
        previous_element = circular_list[(i - 1) % len(circular_list)]

        # Check if the product of the current element and its predecessor is equal to -41
        if current_element * previous_element == -41:
            # Initialize an empty list to store the sublist
            sublist = []

            # Iterate over the elements of the circular list from the current element to the end of the list
            for j in range(i, len(circular_list)):
                # Get the current element and add it to the sublist
                element = circular_list[j]
                sublist.append(element)

                # Check if the product of the current element and its predecessor is equal to -41
                if element * previous_element == -41:
                    # Add the sublist to the list of sublists
                    sublists.append(sublist)

                    # Break out of the inner loop since a sublist has been found
                    break

        # Check if the product of the current element and its predecessor is equal to -41
        if previous_element * current_element == -41:
            # Initialize an empty list to store the sublist
            sublist = []

            # Iterate over the elements of the circular list from the beginning of the list to the current element
            for j in range(0, i + 1):
                # Get the current element and add it to the sublist
                element = circular_list[j]
                sublist.append(element)

                # Check if the product of the current element and its predecessor is equal to -41
                if element * previous_element == -41:
                    # Add the sublist to the list of sublists
                    sublists.append(sublist)

                    # Break out of the inner loop since a sublist has been found
                    break

    return sublists
