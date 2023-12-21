
def lists_with_product_equal_n(circular_list):
    # Create an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the circular list
    for i in range(len(circular_list)):
        # Get the current element and its index
        element = circular_list[i]
        index = i

        # If the product of the sublist is equal to 29, add it to the sublists list
        if product == 29:
            sublists.append(sublist)

        # Iterate over the remaining elements of the circular list
        for j in range(i + 1, len(circular_list)):
            # Get the current element and its index
            element = circular_list[j]
            index = j

            # Add the element to the sublist
            sublist.append(element)

            # Calculate the product of the sublist
            product = 1
            for k in range(len(sublist)):
                product *= sublist[k]

            # If the product of the sublist is equal to 29, add it to the sublists list
            if product == 29:
                sublists.append(sublist)

    # Return the sublists list
    return sublists
