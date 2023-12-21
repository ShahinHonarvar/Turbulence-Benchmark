
def lists_with_product_equal_n(circular_list):
    # Find the product of all elements in the list
    product = 1
    for element in circular_list:
        product *= element

    # Initialize an empty list to store the sublists

    sublists = []

    # Iterate over the list and find contiguous sublists whose product is equal to n

    for i in range(len(circular_list)):

        # Initialize a variable to keep track of the current product

        current_product = 1

        # Initialize a variable to keep track of the starting index of the current sublist

        start_index = i

        # Iterate over the remaining elements in the list

        for j in range(i, len(circular_list)):

            # Update the product and the ending index of the current sublist

            current_product *= circular_list[j]

            if current_product == n:

                # Add the current sublist to the list of sublists

                sublists.append(circular_list[start_index:j+1])

                # Break out of the inner loop since we have found a sublist whose product is equal to n

                break


            # If the product exceeds n, then we know that the current sublist is not the one we are looking for

            if current_product > n:

                break


    return sublists
