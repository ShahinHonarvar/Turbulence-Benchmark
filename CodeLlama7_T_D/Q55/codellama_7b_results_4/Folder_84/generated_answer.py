
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the circular list and calculate the product of adjacent elements
    for i in range(len(circular_list))):
        product = 1

        # Calculate the product of adjacent elements in the circular list
        for j in range(i, len(circular_list)))
            product *= circular_list[j]

            # Check if the product equals -906. If yes, add the sublist to the returned list
            if product == -906:
                sublists.append(circular_list[i:j+1])

                # Check if there are duplicates of such a sublist. If yes, add all such sublists to the returned list
                for k in range(j+1, len(circular_list))):
                    if circular_list[i:k+1] in sublists:
                        sublists.append(circular_list[i:k+1])

            # If no such sublist exists, return an empty list
            else:
                return []

    # Return the list of sublists that satisfy the condition
    return sublists
