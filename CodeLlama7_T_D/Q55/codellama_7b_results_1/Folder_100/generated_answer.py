
def lists_with_product_equal_n(circular_list, n):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements in the circular list
    for i in range(len(circular_list)):

        # Initialize a variable to store the product of the current sublist
        product = 1

        # Initialize a variable to store the size of the current sublist
        size = 0

        # Iterate over the elements in the circular list starting from the current index
        for j in range(i, len(circular_list)):

            # Multiply the current element by the product variable
            product *= circular_list[j]

            # Increment the size of the sublist
            size += 1

            # Check if the product of the elements in the current sublist is equal to n
            if product == n:

                # Append the current sublist to the list of sublists
                sublists.append(circular_list[i : i + size])

                # Break out of the inner loop since we have found a sublist with the desired product
                break

            # Check if the product of the elements in the current sublist is greater than n
            elif product > n:

                # Since the product of the elements in the current sublist is greater than n, we know that no further elements can be added to the sublist without making it larger than the size of the given list. So, we break out of the inner loop.
                break

    # Return the list of sublists
    return sublists
