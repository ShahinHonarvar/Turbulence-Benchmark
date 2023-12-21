
def lists_with_product_equal_n(circular_list):
    # Create an empty list to store the sublists
    sublists = []

    # Iterate over the circular list and find contiguous integers with product equal to n

    for i in range(len(circular_list)):

        # Initialize a variable to store the current product

        current_product = 1

        # Initialize a variable to store the start index of the sublist

        start_index = i

        # Iterate over the circular list from the current index to the end of the list

        for j in range(i, len(circular_list)):

            # Multiply the current product by the current integer

            current_product *= circular_list[j]

            # If the current product is equal to n, add the sublist to the list of sublists

            if current_product == n:
                sublists.append(circular_list[start_index:j+1])

                # Reset the start index and current product

                start_index = j + 1
                current_product = 1

                break

            # If the current product is greater than n, exit the loop

            if current_product > n:
                break

    return sublists
